import os
import json
import pandas as pd
from datetime import datetime
from uuid import uuid4


class MiniDeltaTable:

    ## Initialises the table path and log path
    def __init__(self, table_path:str):
        self.table_path=table_path
        self.log_path=os.path.join(table_path, "_delta_log")
        os.makedirs(self.log_path, exist_ok=True)

    ## Gets the list of existing logs and returns the name/number of next log (used for version controling)
    def _get_next_version(self):
        existing_logs=sorted([int(f.replace(".json", "")) for f in os.listdir(self.log_path) if f.endswith(".json")])
        return (existing_logs[-1]+1) if existing_logs else 0 ## Returns the number/name of next log to be created
    
    def insert(self, df:pd.DataFrame, strict_schema:bool=False):
        version=self._get_next_version()

        if strict_schema and version>0:
            previous_metadata_file=os.path.join(self.log_path, f"{version-1}.json")
            with open(previous_metadata_file, "r") as metadatafile:
                previous_metadata=json.load(metadatafile)
            previous_schema=set(previous_metadata["schema"])
            current_schema=set(df.columns)

            if previous_schema!=current_schema:
                raise ValueError(f"Schema mismatch between current and previous files \n " \
                f"Missing Columns : {previous_schema-current_schema} \n"\
                    f"Additional Columns : {current_schema-previous_schema}")

        version_file=f"data_v_{version}.parquet"
        df.to_parquet(os.path.join(self.table_path, version_file), index=False)

        metadata={
            "version":version,
            "file":version_file,
            "number_of_rows":len(df),
            "schema":list(df.columns),
            "timestamp":datetime.now().isoformat()
        }
        with open(os.path.join(self.log_path, f"{version}.json"), "w") as metadata_file:
            json.dump(metadata, metadata_file, indent=2)
    
    def read(self, version=None):
        if version is None:
            version=self._get_next_version()-1
        with open(os.path.join(self.log_path, f"{version}.json"), "r") as versiondata:
            metadata=json.load(versiondata)
        return pd.read_parquet(os.path.join(self.table_path, metadata["file"]))
    
    def getVersionHistory(self):
        logs=[]
        for f in os.listdir(self.log_path):
            if f.endswith(".json"):
                with open(os.path.join(self.log_path, f)) as jf:
                    logs.append(json.load(jf))
        return pd.DataFrame(logs)
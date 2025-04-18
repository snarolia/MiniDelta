import typer
import pandas as pd
from mini_delta import MiniDeltaTable

app = typer.Typer()

@app.command()
def insert(table_path:str, csv_path:str):
    """Insert data from csv file to delta table"""
    df=pd.read_csv(csv_path)
    delta=MiniDeltaTable(table_path)
    delta.insert(df)
    typer.echo(f"Data from {csv_path} inserted into delta table at path {table_path}")

@app.command()
def read(table_path:str, version:int=None):
    delta=MiniDeltaTable(table_path=table_path)
    df=delta.read(version=version)
    typer.echo(df.to_string(index=False))

@app.command()
def history(table_path:str):
    delta=MiniDeltaTable(table_path=table_path)
    versionHistory=delta.getVersionHistory()
    typer.echo(versionHistory.to_string(index=False))

if __name__=="__main__":
    app()
from mini_delta import MiniDeltaTable
import pandas as pd

delta_table=MiniDeltaTable(table_path="/Users/siddharthnarolia/Projects/Github/MiniDelta/testing_modules/sample_data")


"""Testing Insert of New Data"""
# df_1=pd.DataFrame({
#     "name":["Oliver", "Bruce", "Barry"],
#     "id":[1,2,3],
#     "vigilante_status":["Active", "Active", "Not Active"]
# })
# df_2=pd.DataFrame({
#     "name":["Oliver", "Bruce", "Barry"],
#     "id":[1,2,3],
#     "vigilante_status":["Active", "Not Active", "Not Active"]
# })
# delta_table.insert(df=df_1)
# delta_table.insert(df=df_2)

# print(delta_table.read(version=0))
# print(delta_table.read(version=1))
# print(delta_table.getVersionHistory())

"""Testing Strict Schema Check"""

# df_3=pd.DataFrame({
#     "complete_name":["Sidd"]
# })
# delta_table.insert(df=df_3, strict_schema=True)
#from mini_delta import MiniDeltaTable
import pandas as pd
import random

#delta_table=MiniDeltaTable(table_path="/Users/siddharthnarolia/Projects/Github/MiniDelta/testing_modules/sample_data")


first_names=["John", "Jane", "Alice", "Bob", "Mike", "Sara"]
last_names=["Smith", "Johnson", "Williams", "Brown", "Jones", "Davis"]

data=[]

for i in range(10):
    first=random.choice(first_names)
    last=random.choice(last_names)
    name=f"{first} {last}"
    age=random.randint(18,60)
    email=f"{first.lower()}.{last.lower()}@testmail.com"

    data.append({
        "name":name,
        "age":age,
        "email":email
    })
df=pd.DataFrame(data)
print(df)

df.to_csv("/Users/siddharthnarolia/Projects/Github/MiniDelta/sample_data/csv/sample_data.csv")

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
import pandas as pd

df1=pd.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

print(df1, "\n")
print(df1.mean(), "\n")

df2=pd.DataFrame([{"Name":"John", "Surname":"Smith"},{"Name":"Jack", "Surname":"Bean"}],index=["1","2"])

print(df2, "\n")

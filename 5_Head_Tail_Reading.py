import pandas as pd

df=pd.read_excel("Home_Data.xlsx")
print("Head 2 Rows")
print(df.head(2))
print()
print("Tail 2 Rows")
print(df.tail(2))
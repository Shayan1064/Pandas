import pandas as pd

data=pd.read_excel("SalesData.xlsx")
print(data)

groupcity=data.groupby("City")["Price"].sum()
print(groupcity)

groupProduct=data.groupby("Product")["Price"].sum()
print(groupProduct)


groupp=data.groupby("City")["Price"].mean()
print(groupp)
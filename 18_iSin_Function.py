import pandas as pd


read=pd.read_excel("SalesData.xlsx")
print(read)

filter=read[read["City"].isin(["Lahore","Karachi"])]
print(filter)

# Example 2: Exclude specific cities
exclude_city = read[~read["City"].isin(["Lahore"])]
print("\nExclude Lahore:\n", exclude_city)


both=read[(read["City"].isin(["Lahore"]) & read["Product"].isin(["Laptop"]))]
print(both)
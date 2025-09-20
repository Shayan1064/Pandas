import pandas as pd

data=pd.read_excel("Softmatic.xlsx")
print(data)

#single column
# print(data["Name"])



# multiple columns
subset=data[["Name","Age"]]
print(subset)
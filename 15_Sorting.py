import pandas as pd

data = pd.read_excel("Softmatic.xlsx")
print(data)

top=data[["Name","Salary"]].sort_values(by="Salary", ascending=False)
print(top)

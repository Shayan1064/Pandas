import pandas as pd

data=pd.read_excel("EmployeeData.xlsx")
print(data)


# Upadating Entire Column...
data["Salary"]=data["Salary"]*1.10
print(data)

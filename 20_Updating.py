import pandas as pd

data=pd.read_excel("EmployeeData.xlsx")
print(data)

data.loc[5,"Salary"]=65000
print(data)


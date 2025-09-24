import pandas as pd

data=pd.read_excel("EmployeeData.xlsx")
print(data)


# adding column diectly

data["Bonus"]=data["Salary"]*0.1
data["Total_Salary"]=data["Salary"]+data["Bonus"]
print(data)

# Another Method mean according to location.....

data.insert(0, "ID", [11, 22, 44, 55, 66, 77, 88, 99])
print(data)


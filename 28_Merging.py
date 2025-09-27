import pandas as pd


# Dictionary 1: Employee Basic Info
employees1 = {
    "EmpID": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Sara", "Usman", "Zara", "Amir"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}

# Dictionary 2: Employee Salary Info
employees2 = {
    "EmpID": [3, 4, 5, 6, 7],
    "Salary": [50000, 60000, 55000, 45000, 70000],
    "Location": ["Lahore", "Karachi", "Islamabad", "Multan", "Quetta"]
}

data1=pd.DataFrame(employees1)
data2=pd.DataFrame(employees2)

# write how outer,inner,right,left.......
merged=pd.merge(data1,data2,on="EmpID", how="left")
print(merged)
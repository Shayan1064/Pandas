import pandas as pd

data=pd.read_excel("Softmatic.xlsx")
print(data)

print(" Single row condition")
salary=data[data["Salary"] > 60000]
print(salary)
print()
print("# Multi conditions")
salary_age = data[(data["Salary"] > 60000) & (data["Age"] > 25)]
print(salary_age)


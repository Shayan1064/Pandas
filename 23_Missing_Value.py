import pandas as pd
# Dictionary with 10 employees and some missing values
employees = {
    1: {"Name": "Ali",   "Age": 25, "Salary": 40000},
    2: {"Name": "Sara",  "Age": None, "Salary": 50000},
    3: {"Name": None,    "Age": 30, "Salary": 45000},
    4: {"Name": "Hina",  "Age": 28, "Salary": None},
    5: {"Name": "Usman", "Age": 35, "Salary": 60000},
    6: {"Name": "Zara",  "Age": None, "Salary": None},
    7: {"Name": "Amir",  "Age": 40, "Salary": 70000},
    8: {"Name": None,    "Age": 22, "Salary": 30000},
    9: {"Name": "Nida",  "Age": 27, "Salary": None},
    10: {"Name": "Fahad", "Age": None, "Salary": 55000}
}

data=pd.DataFrame(employees)
data.to_excel("Shayan.xlsx")
print(data)

# To find where is null values in dataset
# print(data.isnull())
print(data.isnull().sum())

# wnat to know how many values are missing

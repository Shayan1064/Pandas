import pandas as pd

# Employee dictionary
employees = {
    1: {"Name": "Shayan", "Age": 22, "Salary": 50000, "Location": "Peshawar"},
    2: {"Name": "Noman", "Age": 25, "Salary": 60000, "Location": "Islamabad"},
    3: {"Name": "Sanan", "Age": 28, "Salary": 55000, "Location": "Lahore"},
    4: {"Name": "Hamdan", "Age": 24, "Salary": 48000, "Location": "Karachi"},
    5: {"Name": "Ayyan", "Age": 23, "Salary": 45000, "Location": "Swabi"},
    6: {"Name": "Ali", "Age": 27, "Salary": 70000, "Location": "Rawalpindi"},
    7: {"Name": "Usman", "Age": 30, "Salary": 80000, "Location": "Quetta"},
    8: {"Name": "Zain", "Age": 26, "Salary": 52000, "Location": "Multan"},
    9: {"Name": "Ahmed", "Age": 29, "Salary": 65000, "Location": "Faisalabad"},
    10: {"Name": "Bilal", "Age": 31, "Salary": 90000, "Location": "Hyderabad"}
}

# Convert dictionary → DataFrame
df = pd.DataFrame.from_dict(employees, orient="index")

# Save to Excel
df.to_excel("Softmatic.xlsx", index=False)

# Read back Excel file
data = pd.read_excel("Softmatic.xlsx")

print(data)

print(data.describe())
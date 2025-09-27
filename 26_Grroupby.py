import pandas as pd

employees = {
    1: {"Name": "Ali",    "Role": "Software Engineer", "Salary": 80000, "Location": "Lahore"},
    2: {"Name": "Sara",   "Role": "Data Analyst",      "Salary": 70000, "Location": "Karachi"},
    3: {"Name": "Usman",  "Role": "AI Engineer",       "Salary": 120000, "Location": "Islamabad"},
    4: {"Name": "Zara",   "Role": "ML Engineer",       "Salary": 110000, "Location": "Lahore"},
    5: {"Name": "Amir",   "Role": "Software Engineer", "Salary": 90000, "Location": "Karachi"},
    6: {"Name": "Nida",   "Role": "Data Analyst",      "Salary": 65000, "Location": "Peshawar"},
    7: {"Name": "Fahad",  "Role": "AI Engineer",       "Salary": 115000, "Location": "Islamabad"},
    8: {"Name": "Hina",   "Role": "ML Engineer",       "Salary": 105000, "Location": "Multan"},
    9: {"Name": "Shayan", "Role": "Software Engineer", "Salary": 95000, "Location": "Quetta"},
    10: {"Name": "Ayesha","Role": "Data Analyst",      "Salary": 72000, "Location": "Lahore"}
}

data = pd.DataFrame.from_dict(employees, orient="index")

print("=== Employee Data ===")
print(data)

group = data.groupby("Role")["Salary"].sum().sort_values(ascending=False)
print("\n=== Total Salary by Role ===")
print(group)

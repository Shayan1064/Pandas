import pandas as pd

import pandas as pd

# Load dataset
data = pd.read_excel("Softmatic.xlsx")
print("Full Dataset:")
print(data)

# =========================
# 🎯 Fetch Columns
# =========================
print("\n--- Fetching Columns ---")
print(data["Name"])              # Single column
print(data[["Name", "Salary"]])  # Multiple columns

# =========================
# 🎯 Fetch Rows
# =========================
print("\n--- Fetching Rows ---")
print(data.iloc[0])     # First row (index 0)
print(data.iloc[3])     # Fourth row
print(data.iloc[:5])    # First 5 rows (slicing)

# =========================
# 🎯 Fetch Rows + Columns
# =========================
print("\n--- Fetching Specific Row + Column ---")
print(data.loc[0, "Name"])   # First row, "Name" column
print(data.iloc[2, 2])       # 3rd row, 3rd column (by index)
print(data.iloc[4,7])


# Shayan Learning Pandas...........!
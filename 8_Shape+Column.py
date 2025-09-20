import pandas as pd

data=pd.read_excel("Softmatic.xlsx")
print(data)

print(f"Shape: {data.shape}")
print(f"Column Names: {data.columns}")


import pandas as pd

data=pd.read_excel("DuplicatesData.xlsx")
print(data)

print()
print("Removed Duplicates...!")
cleaned=data.drop_duplicates(subset='City')
print(cleaned)
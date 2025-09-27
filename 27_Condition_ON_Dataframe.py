import pandas as pd


data=pd.read_excel("Softmatic.xlsx")
print(data)


iff=data["Location"]=="Lahore"
print(iff)
count_lahore=iff.sum()
print(count_lahore)


filtered = data[(data["Salary"] > 60000) & (data["Age"] > 27)]
print(filtered)

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("Softmatic.xlsx")
print(data)


iff=data["Location"]=="Lahore"
print(iff)

total=data["Location"].value_counts()
print(total)
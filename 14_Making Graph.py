import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Softmatic.xlsx")
print(data)

# Check Lahore
iff = data["Location"] == "Lahore"
print(iff)

# Plot value counts
data["Location"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Location")
plt.show()
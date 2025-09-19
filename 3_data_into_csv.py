import pandas as pd

data={
    "Name":["Shayan","Noman","Sanan","Hamdan","ayyan"],
    "City":["Swabi","Dagi","Lahore","Swabi","Rashaka"],
    "age":[11,22,33,44,55]
}
df=pd.DataFrame(data)
print(df)

df.to_csv("Home_Data")
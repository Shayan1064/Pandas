import pandas as pd

employee={
    "Name":["Shayan","Nomman","Sanan","Hamdan","Waheed"],
    "Age":[10,20,None,40,None]
    
}
# how to fill none values with estimated values.....
data=pd.DataFrame(employee)
print("Before Interpolation: ")
print(data)
print()
print("After Interpolation")
data["Age"]=data["Age"].interpolate(method="linear")
print(data)
import pandas as pd

data = {"Name": ["Amit", "Rahul", "Sneha", "Priya"],"Age": [17, 20, 15, 22]}

df = pd.DataFrame(data)

df["Eligible"] = ["Yes" if age >= 18 else "No" for age in df["Age"]]

print(df)
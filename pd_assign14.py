import pandas as pd

data = {"Student": ["Amit", "Rahul", "Sneha", "Priya"],"Marks": [80, 95, 88, 70]}

df = pd.DataFrame(data)

print(df)

print("\nIndex of maximum marks:",df["Marks"].idxmax())
print("Index of minimum marks:",df["Marks"].idxmin())

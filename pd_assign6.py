import pandas as pd

data = {"Name": ["Amit", "Rahul", "Priya", "Sneha"],"Marks": [45, 82, 67, 35]}

df = pd.DataFrame(data)
print(df)
print(df["Marks"]>60)



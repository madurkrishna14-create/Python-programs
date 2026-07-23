import pandas as pd

data = {"Name": ["Amit", "Rahul"],"Age": [20, 21]}

df = pd.DataFrame(data)

df.columns=df.columns.str.lower()
print(df)
df.columns=df.columns.str.upper()

print(df)
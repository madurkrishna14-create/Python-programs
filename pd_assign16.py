import pandas as pd

data = {"Name": ["Amit", "Rahul", "Sneha"],"Age": [20, 21, 22],}

df = pd.DataFrame(data)

print("Original DataFrame:\n",df)

df = df.drop(["Age"], axis=1)

print("\nAfter Dropping Columns:\n",df)

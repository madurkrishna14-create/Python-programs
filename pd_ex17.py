import pandas as pd

df = pd.DataFrame({"Roll": [101, 102, 103],"Name": ["Krishna", "Rahul", "Amit"]})

df = df.set_index("Roll")

print(df)
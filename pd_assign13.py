import pandas as pd

data = {"Marks1": [80, 70, 90],"Marks2": [60, 65, 85]}

df = pd.DataFrame(data)

df["Difference"] = df["Marks1"] - df["Marks2"]

print(df)
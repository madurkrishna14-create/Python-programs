import pandas as pd

df = pd.DataFrame({"Name": [" Krishna ", " Rahul ", " Amit "]})

df["Name"] = df["Name"].str.strip()

print(df)
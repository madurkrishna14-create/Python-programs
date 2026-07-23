import pandas as pd

data = {"Code": ["A-101", "B-202", "C-303"]}

df = pd.DataFrame(data)

df[["Letter", "Number"]] = df["Code"].str.split("-", expand=True)

print(df)
import pandas as pd

data = {"City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune"]}

df = pd.DataFrame(data)

print(df["City"].value_counts())
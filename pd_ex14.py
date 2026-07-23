import pandas as pd

df = pd.DataFrame({"A": [1, 2],"B": [3, 4]})

df.columns = ["X", "Y"]
df.index = ["Row1", "Row2"]

print(df)
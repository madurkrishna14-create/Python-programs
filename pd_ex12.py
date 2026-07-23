import pandas as pd

df = pd.DataFrame({"Math": [80, 90],"Science": [85, 95]}, index=["Krishna", "Rahul"])

print(df)

print(df.stack())

print(df.stack().unstack())

print(pd.melt(df.reset_index(), id_vars="index"))
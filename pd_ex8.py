import pandas as pd

df = pd.DataFrame({"Phone": ["987-654", "123-456", "555-999"]})

df["Phone"] = df["Phone"].replace("-","",regex=True)

print(df)
import pandas as pd
df=pd.DataFrame({"Marks":[10,20,30,40,50]})
print(df.columns)
df.columns=["Score"]
print(df)
import pandas as pd
df1=pd.DataFrame({"Marks": [45,50,60,70]})
df2=[]
for i in df1["Marks"]:
    df2.append(i)
print(df2)
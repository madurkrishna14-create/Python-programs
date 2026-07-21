import pandas as pd
s=pd.Series([10,15,18,22])
df=pd.DataFrame(s)
df.columns=['List1']
df['List2']=20
df['List3']=df['List1']+df['List2']
print(df)
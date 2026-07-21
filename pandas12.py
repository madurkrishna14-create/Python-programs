import pandas as pd
dic={'Name':['Sachin Bharadwaj','Virat kohli','Mahendra singh'],
     'Age':[40,50,45]}
df=pd.DataFrame(dic,index=[True,False,True])
print(df)
print(df.loc[True])
print(df.iloc[1])
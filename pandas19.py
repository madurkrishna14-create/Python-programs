import pandas as pd
dic1={'id':['1','2','3','4','5'],'Value1':['A','C','E','G','I'],
      'Value2':['B','D','F','H','J']}
dic2={'id':['2','3','6','7','8'],'Value1':['K','M','O','Q','S'],
      'Value2':['L','N','P','R','T']}
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
df3=pd.merge(df1,df2,right_index=True,left_index=True)
print(df3)
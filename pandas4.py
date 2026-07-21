import pandas as pd
empdata={'Empid':[101,102,103,104,105],
         'Ename':['Sachin','Vinod','Mahendra','Virat','Chetan'],
         'Doj':['12-07-2015','15-07-2012','13-07-2015','21-07-2017','25-08-2017']}
df=pd.DataFrame(empdata)
print(df[['Empid','Ename']])

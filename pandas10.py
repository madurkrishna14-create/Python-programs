import pandas as pd
Runs={'TCS':{'Qtr1':2500,'Qtr2':2000,'Qtr3':3000,'Qtr4':2500},
      'Wipro':{'Qtr1':2800,'Qtr2':2400,'Qtr3':3600,'Qtr4':2400},
      'L&T':{'Qtr1':2100,'Qtr2':5700,'Qtr3':3500,'Qtr4':2100}}
df=pd.DataFrame(Runs)
print(df)
print(df.head())
print(df.tail())
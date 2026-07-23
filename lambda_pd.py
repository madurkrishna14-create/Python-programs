import pandas as pd
s=pd.Series([i for i in range(20)])
print(s[lambda s: [True if i%2==1 else False for i in range (s.size)]])
print(s.loc[lambda s:[True if i%2==1 else False for i in range (s.size)]])
print(s.iloc[lambda s:[True if i%2==1 else False for i in range (s.size)]])
print(s.get(lambda s:[True if i%2==1 else False for i in range (s.size)]))
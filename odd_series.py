import pandas as pd
s=pd.Series([i for i in range(20)])
def odd(s):
    return [True if i%2==0 else False for i in range(s.size)]
print(s[odd])

s2=pd.Series([10,20,30,40,50])
print(s2.is_monotonic_decreasing)

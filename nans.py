import pandas as pd
s1 = pd.Series([10,20,30,40]) 
s2 = pd.Series([40,30,20,10,pd.NA])
s3 = pd.Series([10,20,40,30,None]) 

print(s1.hasnans)
print(s2.hasnans)
print(s3.hasnans)
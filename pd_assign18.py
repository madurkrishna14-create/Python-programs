import pandas as pd
import numpy as np
array1=np.array([10,20,30,40,50])
dic={"Name":"Krishna","Age":19}
list1=[1,2,3,4,5]
array2=np.arange(1,11,1)
s1=pd.Series(array1)
s2=pd.Series(dic)
s3=pd.Series(list1)
s4=pd.Series(array2)
print(s1)
print(s2)
print(s3)
print(s4)
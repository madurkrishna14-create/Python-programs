import pandas as pd
import numpy as np
s1 = pd.Series(['Sunny','Chinny','Vinny','Pinny','Nikhil','Sunny','Chinny',np.nan])
print(s1) 
print('The Number of unique values with NaN ignore:',s1.nunique()) 
#5
print('The Number of unique values without NaN ignore:',s1.nunique(dropna=False))
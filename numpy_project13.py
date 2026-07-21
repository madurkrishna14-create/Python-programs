import numpy as np
t=np.array([500,-300,1000,-400,700,-200])
print(t.sum())
print(t[t>0])
print(t[t<0])
print(t[t>0].max())
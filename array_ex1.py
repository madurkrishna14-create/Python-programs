import numpy as np
allzeros=np.zeros((5, 5),dtype=int)
allones=np.ones((3, 4),dtype=int)
identity=np.identity(4,dtype=int)
array1=np.arange(10,51)
array2=np.arange(0,1,0.1)

print("All Zeros Array:\n", allzeros)
print("All Ones Array:\n", allones)
print("Identity Matrix:\n", identity)
print("Array from 10 to 50:\n", array1)
print("Array from 0 to 1 with step 0.1:\n", array2)
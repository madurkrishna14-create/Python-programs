import numpy as np
array1=np.array([[1, 2, 3], [4, 5, 6]])
array2=np.zeros((2,3))
array3=np.concatenate((array1,array2),axis=0)
print("Concatenated array:",array3)
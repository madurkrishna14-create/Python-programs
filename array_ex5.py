import numpy as np
array1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Array1 (1D): \n", array1)
print("Even numbers in array1: ", array1[array1%2==0])
print("Numbers greater than 10 in array1: ", array1[array1>10])
array1[array1>5]=0
print("Replace numbers greater than 5 with 0 in array1: ", array1)
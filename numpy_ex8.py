import numpy as np
allzeros=np.zeros(10)
myarray1=np.array([[2.7,-2,-19], [0,3.4,99.9],[10.6,0,13]])
myarray2=np.arange(4,64,4,dtype=np.float32).reshape(3,5)
myarray2A, myarray2B, myarray2C, myarray2D, myarray2E = np.split(myarray2, 5, axis=1)

print(myarray2A)
print(myarray2B)
print(myarray2C)
print(myarray2D)
print(myarray2E)

zerosA, zerosB, zerosC, zerosD, zerosE = np.split(allzeros, [2, 5, 7, 8])

print(zerosA)
print(zerosB)
print(zerosC)
print(zerosD)
print(zerosE)

newarray = np.concatenate((myarray2A, myarray2B, myarray2C), axis=1)

print(newarray)
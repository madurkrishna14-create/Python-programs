import numpy as np
allzeros=np.zeros(10)
vowels=np.array(['a','e','i','o','u'])
allones=np.ones((2,5),dtype=np.int32)
myarray1=np.array([[2.7,-2,-19], [0,3.4,99.9],[10.6,0,13]])
myarray2=np.arange(4,64,4,dtype=np.float32).reshape(3,5)
print("Dimensions of myarray1:",myarray1.ndim)
print("Dimensions of myarray2:",myarray2.ndim)
print("Dimensions of allones:",allones.ndim)
print("Dimensions of allzeros:",allzeros.ndim)
print("Dimensions of vowels:",vowels.ndim)

print("Shape of myarray1:",myarray1.shape)
print("Shape of myarray2:",myarray2.shape)
print("Shape of allones:",allones.shape)
print("Shape of allzeros:",allzeros.shape)
print("Shape of vowels:",vowels.shape)

print("Size of myarray1:",myarray1.size)
print("Size of myarray2:",myarray2.size)
print("Size of allones:",allones.size)
print("Size of allzeros:",allzeros.size)
print("Size of vowels:",vowels.size)

print("Data type of myarray1:",myarray1.dtype)
print("Data type of myarray2:",myarray2.dtype)
print("Data type of allones:",allones.dtype)
print("Data type of allzeros:",allzeros.dtype)
print("Data type of vowels:",vowels.dtype)

print("Item size of myarray1:",myarray1.itemsize)
print("Item size of myarray2:",myarray2.itemsize)
print("Item size of allones:",allones.itemsize)
print("Item size of allzeros:",allzeros.itemsize)
print("Item size of vowels:",vowels.itemsize)

print("b: ",allones.reshape(1,10))

print("c: ",vowels[1:3])

print("d: ",myarray1[1:3])

print("e: ", myarray2[:, :2])

print("f: ", myarray1[1:3, 0])

print("g: ", vowels[::-1])



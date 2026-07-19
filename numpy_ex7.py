import numpy as np
vowels=np.array(['a','e','i','o','u'])
allones=np.ones((2,5),dtype=np.int32)
myarray1=np.array([[2.7,-2,-19], [0,3.4,99.9],[10.6,0,13]])
myarray2=np.arange(4,64,4,dtype=np.float32).reshape(3,5)

print("a: ")
print("Transpose of allones:", allones.transpose())
print("\nTranspose of myarray2:", myarray2.transpose())
print("b: ",vowels[::-1])
sorted_array = np.sort(myarray1, axis=0)
print("c: ", sorted_array)
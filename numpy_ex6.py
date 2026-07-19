import numpy as np
allzeros=np.zeros(10)
vowels=np.array(['a','e','i','o','u'])
allones=np.ones((2,5),dtype=np.int32)
myarray1=np.array([[2.7,-2,-19], [0,3.4,99.9],[10.6,0,13]])
myarray2=np.arange(4,40,4,dtype=np.float32).reshape(3,3)

print("a: ",allones/3)

print("b: ",myarray1+myarray2)

sub=myarray1-myarray2

print("c: ",sub)

print("d: ",myarray1*myarray2)

print("e: ",myarray1@myarray2)

print("f: ",myarray1/myarray2)

cube=myarray1**3

print("g: ",cube/2)

print("h: ",np.round(np.sqrt(myarray2)/2,2))


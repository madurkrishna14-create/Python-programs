import numpy as np
array1=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
first,sec,third=np.split(array1,[1,2],axis=0)
print("First array:",first)
print("Second array:",sec)
print("Third array:",third)
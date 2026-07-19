import numpy as np

myarray4 = np.arange(-1, 10.25, 0.25).reshape(15, 3)

part1, part2, part3 = np.split(myarray4, 3, axis=0)

print(part1)
print(part2)
print(part3)
import numpy as np
marks=np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("Marks:", marks)
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Total marks:", np.sum(marks))
print("Above 80:", marks[marks > 80])
print("Sorted marks:", np.sort(marks))
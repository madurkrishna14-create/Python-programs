import numpy as np
salary=np.array([50000, 60000, 55000, 70000, 65000, 80000, 75000, 90000, 85000, 95000])
print("Salary:", salary)
print("Highest salary:", np.max(salary))
print("Lowest salary:", np.min(salary))
print("Average salary:", np.mean(salary))
print("Total salary:", np.sum(salary))
print("Salary above 40000:", salary[salary > 40000])
print("Bonus of 10%:", salary * 1.10)
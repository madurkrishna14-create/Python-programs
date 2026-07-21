import numpy as np
sales=np.array([1500, 2000, 1800, 2200, 2500, 3000, 2800, 3500, 4000, 4500])
print("Sales:", sales)
print("Total sales:", np.sum(sales))
print("Highest sales:", np.max(sales))
print("Lowest sales:", np.min(sales))
print("Average sales:", np.mean(sales))
print("Sales above 2000:", sales[sales > 2000])
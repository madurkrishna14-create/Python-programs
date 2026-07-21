import numpy as np
t=np.array([31, 29, 35, 28, 32, 30, 33, 27, 34, 36])
print("Temperatures:", t)
print("Highest temperature:", np.max(t))
print("Lowest temperature:", np.min(t))
print("Average temperature:", np.mean(t))
print("Temperature above 35:", t[t > 35])
print("Difference between highest and lowest temperature:", np.max(t) - np.min(t))
import numpy as np
steps=np.array([6500,8200,10000,7200,9000,11000,7800])
print("Avg steps: ",steps.mean())
print("Best day: ",steps.argmax()+1)
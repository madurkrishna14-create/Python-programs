import pandas as pd
import numpy as np

data = {"Roll": np.array([101, 102, 103]),"Marks": np.array([85, 90, 78])}

df = pd.DataFrame(data)

print(df)
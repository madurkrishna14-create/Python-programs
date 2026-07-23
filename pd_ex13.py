import pandas as pd

df = pd.DataFrame({"Name":["Krishna", "Rahul"]},index=[10, 20])

print(df.reset_index())
import pandas as pd

df = pd.DataFrame({"Name": ["Krishna", "Rahul", "Amit", "Rohit"],"Marks": [80, 90, 70, 85]})

print(df.sample(2))
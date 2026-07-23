import pandas as pd

df = pd.DataFrame({"Name": ["Krishna", "Rahul"],"Marks": [80, 90]
})
for index, row in df.iterrows():
    print(index, row)
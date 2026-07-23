import pandas as pd

data = [[101, "Krishna"],[102, "Rahul"],[103, "Amit"]]

df = pd.DataFrame(data, columns=["Roll", "Name"])

print(df)
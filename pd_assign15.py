import pandas as pd

data = {"Marks": [80, 95, 88, 70, 91]}

df = pd.DataFrame(data)

print(df.nlargest(3, "Marks"))
print(df.nsmallest(3,"Marks"))
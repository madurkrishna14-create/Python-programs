import pandas as pd

df = pd.DataFrame({"Name": ["Krishna", "Rahul","Mahesh","Krish"]})
print(df[df["Name"].str.contains("Krish")])
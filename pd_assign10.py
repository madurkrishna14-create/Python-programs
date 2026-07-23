import pandas as pd

data = {
    "Name": ["Amit Kumar", "Rahul Sharma", "Priya Patil"]
}

df = pd.DataFrame(data)

df["First_Name"] = df["Name"].str.split().str[0]

print(df)
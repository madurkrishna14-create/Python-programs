import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha"],
    "Gender": ["M", "F", "M", "F"]
}

df = pd.DataFrame(data)
print(df)

gender_map = {"M": "Male","F": "Female"}

df["Gender"] = df["Gender"].map(gender_map)

print(df)
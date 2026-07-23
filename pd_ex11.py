import pandas as pd

df = pd.DataFrame({"Grade": [1, 2, 3]})

grade_name = {1: "A",2: "B",3: "C"}

df["Grade"] = df["Grade"].map(grade_name)

print(df)
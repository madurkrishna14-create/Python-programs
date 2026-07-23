import pandas as pd

students = [(1, "Krishna"),(2, "Rahul"),(3, "Amit")]

df = pd.DataFrame(students, columns=["ID", "Name"])

print(df)
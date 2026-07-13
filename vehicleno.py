import re
s=input("Enter vehicle registration number:")
m=re.fullmatch("TS[012][0-9][A-Z] {2}\d{4}", s)
if m is not None:
    print("valid vehicle registration number")
else:
    print("Invalid vehicle registration number")
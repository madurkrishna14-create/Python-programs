import re
s=input("Enter mobile number:")
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m is not None:
   print("valid mobile number")
else:
    print("invalid mobile number")
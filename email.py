import re
s = input("Enter mail id:")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m is not None:
   print("valid mail id")
else:
    print("invalid mail id")
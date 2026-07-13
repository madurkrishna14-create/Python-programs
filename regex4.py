import re
s = input("Enter pattern to check:")
m = re.match(s, "abcabdefg")
if m!="note":
    print("Match is available at the beginning of the string")
    print("Start index:", m.start(), "and end index:", m.end())
else:
    print("Match is not available at the beginning of the string")

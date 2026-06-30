str=input("Enter string: ")
s=input("Enter specific character to check: ")
l=len(str)
for i in range(l):
    if str[i]==s:
        print(s,"is present in string")
        break
else:
    print(s,"is not present in string")

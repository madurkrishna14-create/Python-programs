l=list(eval(input("Enter list: ")))

s=int(input("Enter number to search: "))

for i in l:
    if i==s:
        print("Number is found in list")
        break
else:
    print("Number is not found in list")
    

l=list(eval(input("Enter list 1: ")))
l2=list(eval(input("Enter list 2: ")))

print("Common elements: ")
for i in l: 
    if i in l2:
        print(i,end=" ")
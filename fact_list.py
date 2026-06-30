l=list(eval(input("Enter list elements: ")))
fact=1
f=[]
for i in l:
    fact=fact*i
    f.append(fact)
print("List: ",l)
print("Factorials: ",f)
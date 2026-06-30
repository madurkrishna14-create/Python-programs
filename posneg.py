l=list(eval(input("Enter list elements: ")))
pcount=0
ncount=0
for i in l:
    if i>0:
        pcount=pcount+1
    else:
        ncount=ncount+1
print("List: ",l)
print("Positive numbers count: ",pcount)
print("Negative numbers count: ",ncount)
l=[3,2,7,5,9]

mn=l[0]
mx=l[0]

for i in l:
    if i>mx:
        mx=i
    if i<mn:
        mn=i
print("Maximum value: ",mx)
print("Minimum value: ",mn)
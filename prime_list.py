l=list(eval(input("Enter list elements: ")))
n=len(l)
p=[]
for i in l:
    count=0
    for j in range(1,n+1):
        if i%j==0:
            count=count+1
    if count==2:
        p.append(i)
print("List: ",l)
print("Prime numbers: ",p)


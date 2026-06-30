n=list(eval(input("Enter list elements: ")))
l=len(n)
sum=0
for i in n:
    sum=sum+i
print("List: ",n)
print("Average of elements: ",sum/l)
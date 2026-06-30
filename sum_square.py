l=list(eval(input("Enter list elements: ")))
sum=0

for i in l:
    i=i*i
    sum=sum+i
print("List: ",l)
print("Sum of squares: ",sum)
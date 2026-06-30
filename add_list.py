list1=list(eval(input("Enter first list: ")))
list2=list(eval(input("Enter second list: ")))

sum=0
for i in list1:
    sum=sum+i
for j in list2:
    sum=sum+j
print("List 1: ",list1)
print("List 2: ",list2)
print("Sum of elements: ",sum)

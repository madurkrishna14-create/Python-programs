list1=list(eval(input("Enter first list: ")))
list2=list(eval(input("Enter second list: ")))

temp=list1
list1=list2
list2=temp

print("After exchange: ")
print("List 1: ",list1)
print("List 2: ",list2)


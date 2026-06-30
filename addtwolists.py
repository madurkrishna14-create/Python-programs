def add(l1,l2):
    s=0
    for i in l1:
        s=s+i
    for j in l2:
        s=s+j
    return s
list1=list(eval(input("Enter first list: ")))
list2=list(eval(input("Enter second list: ")))
s=add(list1,list2)
print("Sum of list elements: ",s)


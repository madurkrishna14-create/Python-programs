l=list(eval(input("Enter list elements: ")))
esum=0
osum=0
for i in l:
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print("List: ",l)
print("Even numbers sum: ",esum)
print("Odd numbers sum: ",osum)
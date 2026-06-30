l=list(eval(input("Enter list: ")))

s=int(input("Enter number to search for repetition: "))

count=0

for i in l:
    if i==s:
        count=count+1
if count>1:
    print("Number is repeated",count,"times")

        
    

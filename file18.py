#search a string in a file
f1=open("list1.txt",'r')
x=input("Enter a string to search in file: ")
for line in f1:
    if line.strip()==x:
        print("String found: ",x)
        break
    else:
        print("String not found")
f1.close()
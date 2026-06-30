l=list(eval(input("Enter list: ")))
largest=l[0]
smallest=l[0]
for i in l:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("List: ",l)
print("Largest element: ",largest)
print("Smallest element: ",smallest)

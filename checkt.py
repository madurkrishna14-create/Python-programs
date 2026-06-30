t=eval(input("Enter tuple elements: "))

s=int(input("Enter element to check in tuple: "))

for i in t:
    if i==s:
        print("Element is present in tuple")
        break
else:
    print("Element is not present in tuple")
s=input("Enter a string: ")

for i in "aeiou":
    s=s.replace(i,"")

print("String without vowels:",s)
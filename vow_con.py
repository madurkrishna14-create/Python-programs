s=input("Enter a string: ")
v=0
c=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v+=1
        else:
            c+=1

print("Vowels =",v)
print("Consonants =",c)
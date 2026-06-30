str=input("Enter string: ")

for i in str:
    if i not in "aeiou":
        str=str.replace(i,"")
        
print("String without consonants: ",str)


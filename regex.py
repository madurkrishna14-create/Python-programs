import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaabababababababababababababa")
for match in matcher:
    count=count+1
    print(match.start(),"...",match.end(),"...",match.group())
print("Number of occurrences: ",count)
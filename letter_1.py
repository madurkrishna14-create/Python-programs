rows = 5
i = 0

while i <=rows:
    j = 0
    while j <= i:
        print(chr(65 + i), end=" ")
        j += 1
    print()
    i += 1
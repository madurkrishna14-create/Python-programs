rows = 6
i = 1

while i <= rows:
    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i += 1
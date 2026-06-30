rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j += 1

    k = 1
    while k <= i*2-i:
        print("*", end="")
        k += 1

    print()
    i += 1
n=int(input("Enter number of rows: "))
sum = 0


for i in range(1, n + 1): 
    sum = sum + i

    for k in range(n - i):
        print("  ", end="")

    for j in range(1, i + 1):
        if j < i:
            print(j, end="+")
        else:
            print(j, end="")

    print(" =", sum)
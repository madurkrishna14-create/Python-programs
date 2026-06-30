rows=5
i=rows

while i>=1:
    j=1
    while j<=rows-i:
        print(" ", end="")
        j+=1

    k=1
    while k<=(2*i-1):
        print("*", end="")
        k+=1

    print()
    i-=1
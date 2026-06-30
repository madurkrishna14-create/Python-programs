n=int(input("Enter number of rows: "))
rows=1
i=1
while rows<=n:
    cols=1
    while cols<=rows:
        if cols%2==0:
            print("*",end="")
        else:
            print("1",end="")
        i=i+1
        cols=cols+1
    print()
    rows=rows+1

        
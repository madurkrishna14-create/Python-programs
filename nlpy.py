rows=5
i=5
while rows>=1:
    cols=5
    while cols>=rows:
        print("*",end="")
        i=i-1
        cols=cols-1
    print()
    rows=rows-1
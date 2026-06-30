def armstrong(n):
    temp=n
    s=0
    while temp>0:
        digit=temp%10
        s=s+digit**3
        temp=temp//10
    if s==n:
        print(f"{n} is armstrong number")
    else:
        print(f"{n} is not armstrong number")
n=int(input("Enter a number: "))
armstrong(n)

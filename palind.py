for num in range(1,101):
    temp=num
    r=0

    while temp>0:
        digit=temp%10
        r=r*10+digit
        temp=temp//10

    if num==r:
        print(num,end=" ")
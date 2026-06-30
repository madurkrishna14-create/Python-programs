def avg_ofdigits(n):
    count=0
    s=0
    while n>0:
        digit=n%10
        s=s+digit
        count=count+1
        n=n//10
    avg=s/count
    print("Average of digits: ",avg)
n=int(input("Enter a number: "))
avg_ofdigits(n)

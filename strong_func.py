import math
def strong_num():
    n=int(input("Enter a number: "))
    temp=n
    s=0
    while temp>0:
        digit=temp%10
        s=s+math.factorial(digit)
        temp=temp//10
    if s==n:
        print(f"{n} is strong number")
    else:
        print(f"{n} is not strong number")
strong_num()
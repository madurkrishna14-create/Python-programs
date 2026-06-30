count=0
for num in range(1,101):
    temp=num
    r=0

    while temp>0:
        digit=temp%10
        r=r*10+digit
        temp=temp//10

    if num==r:
        count=count+1
print("Count of palindrome numbers: ",count)
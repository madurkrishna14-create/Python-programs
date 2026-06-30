def count_digits(n):
    count=0
    while n>0:
        digit=n%10
        count=count+1
        n=n//10
    print("Count of digits: ",count)
n=int(input("Enter a number: "))
count_digits(n)
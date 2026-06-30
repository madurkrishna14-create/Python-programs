def palindrome(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if n==rev:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
n=int(input("Enter a number: "))
palindrome(n)
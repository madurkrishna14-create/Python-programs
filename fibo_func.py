def fibonacci(n):
    first=0
    sec=1
    for i in range(n+1):
        print(first,end=" ")
        next=first+sec
        first=sec
        sec=next
n=int(input("Enter a number: "))
print(f"Fibonacci series till {n} places: ")
fibonacci(n)
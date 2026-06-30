def ci(p,r,n,t):
    amount=p*(1+r/n)**n*t
    print("Compound interest: ",amount)
p=int(input("Enter principal amount: "))
r=int(input("Enter interest rate: "))
n=int(input("Enter no of times interest is compounded: "))
t=int(input("Enter years: "))
ci(p,r,n,t)
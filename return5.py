def sim_com():
    p=int(input("Enter principal amount: "))
    r=int(input("Enter interest rate: "))
    n=int(input("Enter no of times interest is compounded: "))
    t=int(input("Enter years: "))
    si=(p*r*t)/100
    ci=p*(1+r/n)**n*t
    return si,ci
s,c=sim_com()
print("Simple interest: ",s)
print("Compound interest: ",c)

import math
def comp(n,r,p=10000):
    ci=p*math.pow(1+r/100,n)
    print("Ci: ",ci)
comp(5,12.5,1000)
comp(5,12.5)
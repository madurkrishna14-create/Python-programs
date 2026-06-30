import math
def r(a):    
    sq=a*a
    sqrt=math.sqrt(a)
    cube=a**3
    return sq,sqrt,cube
s,sq,c=r(9)
print("Square: ",s)
print("Square root: ",sq)
print("Cube: ",c)

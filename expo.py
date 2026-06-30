def expo(x,y):
    if y==0:
        return 1
    return x*expo(x,y-1)
e=expo(10,3)
print("Exponent: ",e)

import math
def sphere():
    r=int(input("Enter radius: "))
    area=4*math.pi*r*r
    vol=4/3*math.pi*r**3
    return area,vol
a,v=sphere()
print("Area of sphere: ",a)
print("Volume: ",v)
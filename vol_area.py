import math
def volume_area(r):
    a=4*math.pi*r*r
    v=4/3*math.pi*r**3
    print("Area of sphere: ",a)
    print("Volume of sphere: ",v)
r=int(input("Enter radius of sphere: "))
volume_area(r)

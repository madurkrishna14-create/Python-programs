import math
def circle():
    r=int(input("Enter radius: "))
    area=math.pi*r*r
    cir=2*math.pi*r
    return area,cir
a,c=circle()
print("Area of circle: ",a)
print("Circumference: ",c)


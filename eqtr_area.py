import math
def area(s):
    a=math.sqrt(3)/4*s*s
    print("Area of equilateral triangle: ",a)
s=int(input("Enter side of equilateral triangle: "))
area(s)
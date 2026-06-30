def rect():
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    area=l*b
    pr=2*(l+b)
    return area,pr
a,p=rect()
print("Area of rectangle: ",a)
print("Perimeter: ",p)
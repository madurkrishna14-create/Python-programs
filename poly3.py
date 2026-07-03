class Shape:

    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(5), Circle(4)]

for shape in shapes:
    print(shape.area())

class Shape:
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        print("Inside circle")
class Rect(Shape):
    def draw(self):
        print("Inside rect")
class Triangle(Shape):
    def draw(self):
        print("Inside triangle")
c=Circle()
c.draw()
r=Rect()
r.draw()
t=Triangle()
t.draw()
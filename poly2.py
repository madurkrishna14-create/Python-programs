class Bird:

    def fly(self):
        print("Bird flies")

class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies")

class Eagle(Bird):

    def fly(self):
        print("Eagle flies")

birds = [Sparrow(), Eagle()]

for bird in birds:
    bird.fly()

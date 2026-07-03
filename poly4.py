class Printer:

    def print_data(self, *args):
        for item in args:
            print(item)

p = Printer()

p.print_data("Python")
p.print_data("Python", "Java")
p.print_data("Python", "Java", "C++")

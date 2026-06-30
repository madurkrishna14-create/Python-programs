#Super method with constructor without args(Single inheritance)

class Person:
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.gender=input("Enter gender: ")
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll=int(input("Enter roll no: "))
        self.branch=input("Enter branch: ")
    def show(self):
        super().show()
        print("Student roll: ",self.roll)
        print("Branch: ",self.branch)
ob2=Student()
ob2.show()
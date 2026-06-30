class Person:
    def getp(self):
        self.name=input("Enter name: ")
        self.age=input("Enter age: ")
    def showp(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Address():
    def geta(self):
        self.city=input("Enter city: ")
        self.area=input("Enter area: ")
    def showa(self):
        print("City: ",self.city)
        print("Area: ",self.area)
class Student(Person,Address):
    def gets(self):
        self.roll=int(input("Enter roll: "))
        self.cl=int(input("Enter class: "))
    def shows(self):
        print("Student roll no: ",self.roll)
        print("Class: ",self.cl)
ob=Student()
ob.getp()
ob.gets()
ob.geta()
ob.showp()
ob.showa()
ob.shows()
class Person:
    def getp(self):
        self.name=input("Enter name: ")
        self.age=input("Enter age: ")
    def showp(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Address(Person):
    def geta(self):
        self.city=input("Enter city: ")
        self.area=input("Enter area: ")
    def showa(self):
        print("City: ",self.city)
        print("Area: ",self.area)
class Student(Address):
    def gets(self):
        self.cl=input("Enter class: ")
        self.clg=input("Enter college: ")
    def shows(self):
        print("Class: ",self.cl)
        print("College: ",self.clg)
ob=Student()
ob.getp()
ob.geta()
ob.gets()
ob.showp()
ob.showa()
ob.shows()

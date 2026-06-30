class Person:
    def getp(self):
        self.name=input("Enter person name: ")
        self.age=input("Enter age: ")
    def showp(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Student(Person):
    def gets(self):
        self.roll=input("Enter roll no: ")
        self.cl=int(input("Enter class: "))
    def shows(self):
        print("Student name: ",self.roll)
        print("Age: ",self.cl)
class Emp(Person):
    def gete(self):
        self.empid=int(input("Enter emp id: "))
        self.com=input("Enter employee company: ")
    def showe(self):
        print("Emp id: ",self.empid)
        print("Company: ",self.com)
ob=Student()
ob.getp()
ob.gets()
ob2=Emp()
ob2.getp()
ob2.gete()

ob.showp()
ob.shows()

ob2.showp()
ob2.showe()


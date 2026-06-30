class Person:
    def getp(self):
        self.name=input("Enter name: ")
        self.age=input("Enter age: ")
    def showp(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Salary:
    def gets(self):
        self.sal=int(input("Enter salary: "))
    def shows(self):
        print("Salary: ",self.sal)
class Emp(Person,Salary):
    def gete(self):
        self.empid=int(input("Enter emp id: "))
        self.com=input("Enter company: ")
    def showe(self):
        print("Emp id: ",self.empid)
        print("Company: ",self.com)
ob=Emp()
ob.getp()
ob.gets()
ob.gete()
ob.showp()
ob.shows()
ob.showe()
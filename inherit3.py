class Person:
    def getp(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def showp(self):
        print("Person's name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Employee(Person):
    def gete(self,empid,sal,exp):
        self.empid=empid
        self.sal=sal
        self.exp=exp
    def showe(self):
        print("Employee id: ",self.empid)
        print("Salary: ",self.sal)
        print("Exp: ",self.exp)
e=Employee()
e.getp("Krishna",29,"Male")
e.gete(1,200000000,5)
e.showp()
e.showe()
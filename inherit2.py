class Person:
    def getp(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def showp(self):
        print("Student name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Student(Person):
    def gets(self,roll,branch,college):
        self.roll=roll
        self.branch=branch
        self.college=college
    def shows(self):
        print("Student roll: ",self.roll)
        print("Branch: ",self.branch)
        print("College: ",self.college)
s=Student()
s.getp("Krishna",19,"Male")
s.gets("30","Infotech","GPS")
s.showp()
s.shows()

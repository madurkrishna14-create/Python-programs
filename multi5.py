class Student:
    def gets(self):
        self.name=input("Enter student name: ")
        self.age=int(input("Enter age: "))
    def shows(self):
        print("Student name: ",self.name)
        print("Age: ",self.age)
class Sem1(Student):
    def getS1(self):
        self.s1=int(input("Enter semester1 marks: "))
    def showS1(self):
        print("Semester1 marks: ",self.s1)
class Sem2(Sem1):
    def getS2(self):
        self.s2=int(input("Enter semester2 marks: "))
    def showS2(self):
        print("Semester2 marks: ",self.s2)
class Result(Sem2):
    def calc(self):
        self.total=self.s1+self.s2
        self.per=self.total/2
    def showr(self):
        print("Total marks: ",self.total)
        print("Percentage: ",self.per)
ob=Result()
ob.gets()
ob.getS1()
ob.getS2()
ob.calc()
ob.shows()
ob.showS1()
ob.showS2()
ob.showr()
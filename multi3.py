class Student:
    def gets(self):
        self.name=input("Enter student name: ")
        self.age=int(input("Enter age: "))
    def shows(self):
        print("Student name: ",self.name)
        print("Age: ",self.age)
class Test(Student):
    def gett(self):
        self.marks1=int(input("Enter test1 marks: "))
        self.marks2=int(input("Enter test2 marks: "))
    def showt(self):
        print("Test1 marks: ",self.marks1)
        print("Test2 marks: ",self.marks2)
class Sports(Test):
    def getsp(self):
        self.smarks=int(input("Enter sports marks: "))
    def showsp(self):
        print("Sports marks: ",self.smarks)
class Result(Sports):
    def calc(self):
        self.total=self.marks1+self.marks2+self.smarks
        self.per=self.total/3
    def showr(self):
        print("Total marks: ",self.total)
        print("Percentage: ",self.per)
ob=Result()
ob.gets()
ob.gett()
ob.getsp()
ob.calc()
ob.shows()
ob.showt()
ob.showsp()
ob.showr()
    
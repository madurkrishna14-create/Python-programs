class Student:
    def gets(self):
        self.name=input("Enter student name: ")
        self.age=int(input("Enter age: "))
    def shows(self):
        print("Student name: ",self.name)
        print("Age: ",self.age)
class Iexam(Student):
    def getI(self):
        self.imarks=int(input("Enter internal exam marks: "))
    def showI(self):
        print("Internal exam marks: ",self.imarks)
class Eexam(Iexam):
    def getE(self):
        self.emarks=int(input("Enter external exam marks: "))
    def showE(self):
        print("External exam marks: ",self.emarks)
class Result(Eexam):
    def calc(self):
        self.total=self.imarks+self.emarks
        self.per=self.total/2
    def showr(self):
        print("Total marks: ",self.total)
        print("Percentage: ",self.per)
ob=Result()
ob.gets()
ob.getI()
ob.getE()
ob.calc()
ob.shows()
ob.showI()
ob.showE()
ob.showr()

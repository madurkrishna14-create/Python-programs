class Student():
    def gets(self):
        self.name=input("Enter student name: ")
        self.roll=input("Enter roll no: ")
    def shows(self):
        print("Student name: ",self.name)
        print("Roll: ",self.roll)
class Engg(Student):
    def getEngg(self):
        self.year=input("Enter engg year: ")
    def showEngg(self):
        print("Engineering year: ",self.year)
class Medical(Student):
    def getMed(self):
        self.myear=input("Enter medical year: ")
    def showMed(self):
        print("Medical year: ",self.myear)
ob1=Engg()
ob1.gets()
ob1.getEngg()

ob2=Medical()
ob2.gets()
ob2.getMed()

ob1.shows()
ob1.showEngg()

ob2.shows()
ob2.showMed()
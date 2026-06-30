class Student:
    def gets(self,name,roll,branch,m1,m2,m3):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def shows(self):
        print("Student name: ",self.name)
        print("Roll: ",self.roll)
        print("Branch: ",self.branch)
        print("Marks1: ",self.m1)
        print("Marks2: ",self.m2)
        print("Marks3: ",self.m3)
class Test(Student):
    def gett(self,tname,tid):
        self.tname=tname
        self.tid=tid
    def calc(self):
        self.total=self.m1+self.m2+self.m3
        self.per=self.total/3
        if self.per>50:
            self.g="Grade A"
        else:
            self.g="Grade B"
    def showt(self):
        print("Total marks: ",self.total)
        print("Percentage: ",self.per)
        print("Grade: ",self.g)
t=Test()
t.gets("Krishna",30,"Infotech",90,89,88)
t.gett("Unit test 1",10)
t.calc()
t.shows()
t.showt()

    
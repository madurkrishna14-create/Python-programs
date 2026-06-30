#Super method with multilevel inheritance

class Student:
    def get(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def show(self):
        print("Name: ",self.name)
        print("Roll: ",self.roll)
        print("Branch: ",self.branch)
class Test(Student):
    def get(self,name,roll,branch,m1,m2):
        super().get(name,roll,branch)
        self.m1=m1
        self.m2=m2
    def show(self):
        super().show()
        print("Marks1: ",self.m1)
        print("Marks2: ",self.m2)
class Result(Test):
    def calc(self):
        self.total=self.m1+self.m2
        self.per=self.total/2
    def show(self):
        super().show()
        print("Total: ",self.total)
        print("Per: ",self.per)
ob=Result()
ob.get("krishna",31,"infotech",90,89)
ob.calc()
ob.show()
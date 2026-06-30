#Super method with constructor(including args, single inheritance)

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Student(Person):
    def __init__(self,name,age,gender,roll,branch):
        super().__init__(name,age,gender)
        self.roll=roll
        self.branch=branch
    def show(self):
        super().show()
        print("Student roll: ",self.roll)
        print("Branch: ",self.branch)
ob2=Student("ABC",19,"male",31,"infotech")
ob2.show()
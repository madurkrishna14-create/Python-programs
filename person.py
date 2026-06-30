#Super method with single inheritance

class Person:
    def get(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Student(Person):
    def get(self,name,age,gender,roll,branch):
        super().get(name,age,gender)
        self.roll=roll
        self.branch=branch
    def show(self):
        super().show()
        print("Student roll: ",self.roll)
        print("Branch: ",self.branch)
ob2=Student()
ob2.get("ABC",19,"male",31,"infotech")
ob2.show()
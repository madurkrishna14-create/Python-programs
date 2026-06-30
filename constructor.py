class Student:
    def __init__(self,name,roll,per):
        self.name=name
        self.roll=roll
        self.per=per
    def show(self):
        print("Name: ",self.name)
        print("Roll: ",self.roll)
        print("Per: ",self.per)
s=Student("Ram",1,90)
s.show()
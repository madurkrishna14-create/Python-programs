class Student:

    count = 0

    def __init__(self):
        Student.count += 1

s1 = Student()
s2 = Student()
s3 = Student()

print(Student.count)

class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

e1 = Employee("Rahul")
e2 = Employee("Priya")

print(e1.name)
print(e2.name)

print(Employee.company)

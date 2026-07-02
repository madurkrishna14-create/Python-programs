class Student:
    count = 0

    def __init__(self):
        Student.count += 1

for i in range(5):
    Student()

print(Student.count)

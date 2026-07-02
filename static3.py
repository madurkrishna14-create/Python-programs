class Student:
    school = "ABC"

s1 = Student()
s2 = Student()

s1.school = "XYZ"

print(s1.school)
print(s2.school)
print(Student.school)

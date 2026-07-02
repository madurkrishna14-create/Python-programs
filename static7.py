class Student:

    school = "ABC"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ")

print(Student.school)

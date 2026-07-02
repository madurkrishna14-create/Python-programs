class Employee:
    company = "Infosys"

e1 = Employee()
e2 = Employee()

print(e1.company)
print(e2.company)

Employee.company = "TCS"

print(e1.company)
print(e2.company)

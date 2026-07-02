class Employee:
    company = "Microsoft"

e1 = Employee()
e2 = Employee()

Employee.company = "Google"

print(e1.company)
print(e2.company)

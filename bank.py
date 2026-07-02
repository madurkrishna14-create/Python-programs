class Bank:
    bank_name = "State Bank"
    def __init__(self, customer):
        self.customer = customer

c1 = Bank("Rahul")
c2 = Bank("Priya")

print(c1.bank_name)
print(c2.bank_name)

Bank.bank_name = "HDFC Bank"

print(c1.bank_name)
print(c2.bank_name)


class Car:
    wheels = 4

c1 = Car()
c2 = Car()

print(c1.wheels)
print(c2.wheels)

class Car:
    wheels = 4

c1 = Car()
c2 = Car()

print(c1.wheels)
print(c2.wheels)

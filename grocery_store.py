print("----WELCOME TO 7 STAR GROCERY STORE!----")
choice=input("Would you like to start shopping? (Yes/No): ")
if choice=="yes":
    print("Our stock: Milk,Eggs,Bread,Meat")
else:
    exit()
print("Prices: ")
print("Milk per litre: 1.20$")
print("Pack of 12 eggs: 2$")
print("Regular bread packet: 1.50$")
print("Sourdough bread packet: 2.50$")
print("Enter what you want to purchase: ")
milk=int(input("Enter how much milk you want (in litres): "))
eggs=int(input("Enter how many egg packets you want: "))
bread=input("Enter which bread you want(Regular/Sourdough): ")

milk_price=1.20
eggs_price=2
regular_bread=0
sourdough_bread=0

if bread=="regular":
    regular_bread=1.50
    bill=(milk*milk_price)+(eggs*eggs_price)+(regular_bread)
else:
    sourdough_bread=2.50
    bill=(milk*milk_price)+(eggs*eggs_price)+(sourdough_bread)
print(f"Bill: {bill}$")

cash=0
card=0
pay=input("Enter method of payment(Cash/Card): ")
if pay=="cash":
    cash=float(input(f"Please pay {bill}$: "))
else:
    print("Swiping card....")
    card=float(input(f"Please pay {bill}$: "))

if cash==bill:
    print("Your payment is done.Thanks for visitng our store!")
elif card==bill:
    print("Transaction successfull.Thanks for visitng our store!")
else:
    print(f"Please pay the whole amount of {bill}$")









import random
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="!@#$%^&*()_-="

all=uppercase+lowercase+digits+symbols
password=""
print("---PASSWORD GENERATOR---")
length=int(input("Enter password length: "))
for i in range(1,length+1):
    password=password+random.choice(all)
print("Your Password: ",password)

try:
      x=int(input("Enter a number: "))
      y=int(input("Enter a number: "))

      print(x/y)
except (ZeroDivisionError,ValueError) as msg:
      print("Problem: ",msg)

print("After except block")
    
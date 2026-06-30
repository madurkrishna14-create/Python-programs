def wish(name):
    print("Hello: ",name)
greetings=wish
wish("Ram")
greetings("Krishna")
print(id(wish))
print(id(greetings))
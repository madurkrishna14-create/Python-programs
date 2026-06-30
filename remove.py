s = set(eval(input("Enter set: ")))
r = set(eval(input("Enter elements to remove: ")))

s.difference_update(r)

print("Updated set:", s)
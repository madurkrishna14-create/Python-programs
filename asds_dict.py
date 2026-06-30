d=dict(eval(input("Enter values: ")))


print("Ascending: ",dict(sorted(d.items())))

print("Descending: ",dict(sorted(d.items(), reverse=True)))
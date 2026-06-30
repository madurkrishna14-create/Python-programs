rec={}
n = int(input("Enter number of students:"))
i=1
while i<= n:
    name = input("Enter student name: ")
    marks = input("Enter % of marks of student:")
    rec[name] = marks
    i= i+1
print("Name of student", "\t", "% of marks")
for x in rec:
    print("\t",x, "\t\t",rec[x])

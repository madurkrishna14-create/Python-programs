#read content of file without read method
f=open("students.txt",'r')
data=""
for line in f:
    data=line
    print(data)

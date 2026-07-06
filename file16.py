#read only even lines from a file
f1=open("list1.txt",'w')
names=["krishna\n","sanskar\n","chetan\n","prajyot\n","max"]
f1.writelines(names)
f1.close()
f2=open("list1.txt",'r')
line_no=1
for line in f2:
    if line_no%2==0:
        print(line)
    line_no=line_no+1
f2.close()
#read only odd lines from file
f1=open("list1.txt",'r')
line_no=1
for line in f1:
    if line_no%2!=0:
        print(line)
    line_no=line_no+1
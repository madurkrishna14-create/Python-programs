f=open("abc1.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()
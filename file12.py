#Copy contents of one file into another
f1=open("abc1.txt",'r')
f2=open("abc2.txt",'w')
data=f1.read()
f2.write(data)
print("File copied successfully")
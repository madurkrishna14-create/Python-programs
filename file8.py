data="students are learning python"
f=open("abc1.txt",'w')
f.write(data)
with open("abc1.txt",'r+') as f:
    text=f.read()
    print(text)
    print("Current position: ",f.tell)
    f.seek(10)
    f.write("GEMS")
    f.seek(0)
    print("Current position: ",f.tell())


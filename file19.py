#encrypt contents of file
f1=open("list1.txt",'r')
for line in f1:
    enc=""
    for ch in line:
        enc=enc+chr(ord(ch)+5)
    print(enc)
f1.close()
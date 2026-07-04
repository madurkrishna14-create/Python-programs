f1=open("img1.jpeg",'rb')
f2=open("newimg.jpeg",'wb')
bytes=f1.read()
f2.write(bytes)
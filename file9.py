import os,sys
fname=input("Enter file name: ")
if os.path.isfile(fname):
    print("File exists: ",fname)
    f=open(fname,'r')
else:
    print("File doesnt exist")
    sys.exit(0)
print("Content of file is: ")
data=f.read()
print(data)
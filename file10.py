import os,sys
fname=input("Enter file name: ")
if os.path.isfile(fname):
    print("File exists: ",fname)
    f=open(fname,'r')
else:
    print("File doesnt exist")
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
   lcount=lcount+1
   ccount=ccount+len(line)
   words=line.split()
   wcount=wcount+len(words)
print("number of lines: ",lcount)
print("number of words: ",wcount)
print("number of characters: ",ccount)
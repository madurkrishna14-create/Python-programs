class Faculty: 
    def set(self,name,sub,exp):
        self.name=name
        self.sub=sub
        self.exp=exp
    def disp(self):
        print("Faculty name: ",self.name)
        print("Subject: ",self.sub)
        print("Experience: ",self.exp)
f=Faculty()
n=input("Enter faculty name: ")
s=input("Enter subject: ")
e=int(input("Enter experience: "))
f.set(n,s,e)
f.disp()
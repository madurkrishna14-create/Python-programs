class Addition:
    def get(self,a,b):
        self.a=a
        self.b=b
    def calc(self):
        self.s=self.a+self.b
    def disp(self):
        print("Sum: ",self.s)        
a=Addition()
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
a.get(n1,n2)
a.calc()
a.disp()
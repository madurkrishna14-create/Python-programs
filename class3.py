class Data:
    def set(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("a=",self.a)
        print("b=",self.b)
d=Data()
d.set(10,20)
d.show()
x=int(input("Enter no: "))
y=int(input("Enter no: "))
d1=Data()
d1.set(x,y)
d1.show()
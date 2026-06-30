class Demo:
    def set(self):
        self.a=int(input("Enter no: "))
        self.b=int(input("Enter no: "))
    def show(self):
        print("a=",self.a)
        print("b=",self.b)
d=Demo()
d.set()
d.show()
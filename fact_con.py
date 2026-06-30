class Factorial:
    def __init__(self,no):
        self.no=no
        self.fact=1
    def cal(self):
        i=1
        while i<=self.no:
            self.fact=self.fact*i
            i=i+1
    def show(self):
        print("No: ",self.no)
        print("Factorial: ",self.fact)
f=Factorial(5)
f.cal()
f.show()
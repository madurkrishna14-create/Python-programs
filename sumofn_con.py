class Sum:
    def __init__(self,n):
        self.n=n
        self.s=0
    def cal(self):
        i=0
        while i<=self.n:
            self.s=self.s+i
            i=i+1
    def show(self):
        print(f"Sum of numbers till {self.n}: ",self.s)
s=Sum(10)
s.cal()
s.show()
class Sum:
    def __init__(self,n):
        self.n=n
        self.es=0
        self.os=0
    def cal(self):
        i=0
        for i in range(self.n+1):
            if i%2==0:
                self.es=self.es+i
            else:
                self.os=self.os+i
    def show(self):
        print("Even sum: ",self.es)
        print("Odd sum: ",self.os)
s=Sum(10)
s.cal()
s.show()
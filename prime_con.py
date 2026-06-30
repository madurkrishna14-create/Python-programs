class Prime:
    def __init__(self,n):
        self.n=n
        self.count=0
    def cal(self):
        for i in range(1,self.n+1):
            if self.n%i==0:
                self.count=self.count+1
            if self.count==2:
                print(i)
print("Prime numbers: ")
p=Prime(10)
p.cal()

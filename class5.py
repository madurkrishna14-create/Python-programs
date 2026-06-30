class Employee:
    def set(self,name,sal,exp):
        self.name=name
        self.sal=sal
        self.exp=exp
    def disp(self):
        print("Name: ",self.name)
        print("Salary: ",self.sal)
        print("Experience: ",self.exp)
e=Employee()
e.set("Krishna",140000,15)
e.disp()
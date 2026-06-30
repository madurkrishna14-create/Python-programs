class Product:
    def set(self,name,mrp,sp):
        self.name=name
        self.mrp=mrp
        self.sp=sp
    def disp(self):
        print("Product name: ",self.name)
        print("Maximum price: ",self.mrp)
        print("Selling price: ",self.sp)
p=Product()
n=input("Enter product name: ")
m=int(input("Enter maximum price: "))
s=int(input("Enter selling price: "))
p.set(n,m,s)
p.disp()

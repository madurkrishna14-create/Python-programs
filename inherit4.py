class Author:
    def geta(self,name,age):
        self.name=name
        self.age=age
    def showa(self):
        print("Author name: ",self.name)
        print("Age: ",self.age)
class Book(Author):
    def getb(self,bname,price,publisher):
        self.bname=bname
        self.price=price
        self.publisher=publisher
    def showb(self):
        print("Book name: ",self.bname)
        print("Price: ",self.price)
        print("Publisher: ",self.publisher)
b=Book()
b.geta("JK Rowling",55)
b.getb("Harry Potter",1000,"Apex publishers")
b.showa()
b.showb()
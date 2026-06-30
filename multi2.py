class Author:
    def geta(self):
        self.aname=input("Enter author name: ")
        self.age=int(input("Enter age: "))
    def showa(self):
        print("Author name: ",self.aname)
        print("Age: ",self.age)
class Book(Author):
    def getb(self):
        self.bname=input("Enter book name: ")
        self.bid=int(input("Enter book id: "))
    def showb(self):
        print("Book name: ",self.bname)
        print("Book id: ",self.bid)
class Public(Book):
    def getp(self):
        self.pname=input("Enter publication name: ")
        self.pcity=input("Enter publisher's city: ")
    def showp(self):
        print("Publication name: ",self.pname)
        print("City: ",self.pcity)
ob=Public()
ob.geta()
ob.getb()
ob.getp()
ob.showa()
ob.showb()
ob.showp()
    
class Book:
    def data(self,b_name,b_author,b_pub):
        self.b_name=b_name
        self.b_author=b_author
        self.b_pub=b_pub
    def disp(self):
        print("Book name: ",self.b_name)
        print("Book author: ",self.b_author)
        print("Book publisher: ",self.b_pub)
b=Book()
n=input("Enter book name: ")
a=input("Enter author name: ")
p=input("Enter publisher name: ")
b.data(n,a,p)
b.disp()

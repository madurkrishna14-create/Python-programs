class A:
    def show(self):
        pass
    def display(self):
        print("Inside display")
class B(A):
    def show(self):
        print("Inside show")
ob=B()
ob.show()
ob.display()
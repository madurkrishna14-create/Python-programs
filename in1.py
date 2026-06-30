class A:
    def show(self):
        print("Inside class A")
class B(A):
    def show(self):
        super().show()
        print("Inside class B")
ob=B()
ob.show()
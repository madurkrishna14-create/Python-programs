class A:
    def show(self):
        print("in A")
class B(A):
    def disp(self):
        print("in B")
ob=B()
ob.show()
ob.disp()
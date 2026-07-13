class MarksException(Exception):
    def __init__(self,arg):
        self.msg=arg
try: 
    x=int(input("Enter marks: "))
    if x>100 or x<0:
       raise MarksException("Incorrect marks")
    else:
       print(x)
except MarksException as msg:
    print(msg)
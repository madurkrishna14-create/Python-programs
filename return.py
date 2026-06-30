def arith(a,b):
    A=a+b
    S=a-b
    M=a*b
    D=a/b
    R=a%b
    return A,S,M,D,R
x,y,z,u,v=arith(10,5)
print("Sum: ",x)
print("Sub: ",y)
print("Multiplication: ",z)
print("Division: ",u)
print("Remainder: ",v)
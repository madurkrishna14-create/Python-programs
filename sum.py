def sum_n(n):
    s=0
    if n==1:
        return(1)
    return n+sum_n(n-1)
sm=sum_n(10)
print("Sum: ",sm)
   



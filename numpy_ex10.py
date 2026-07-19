import numpy as np

myarray4=np.arange(-1, 10.25, 0.25).reshape(15,3)

print("a) Sum =",np.sum(myarray4))
print("b) Row-wise Sum =",np.sum(myarray4,axis=1))
print("c) Column-wise Sum =",np.sum(myarray4,axis=0))
print("d) Maximum =",np.max(myarray4))
print("e) Minimum of each row =",np.min(myarray4,axis=1))
print("f) Mean of each row =",np.mean(myarray4,axis=1))
print("g) Column-wise Standard Deviation =",np.round(np.std(myarray4,axis=0),2))
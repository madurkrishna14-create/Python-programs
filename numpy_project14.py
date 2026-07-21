import numpy as np
m=np.array([[78,90,40],[66,45,80],[47,77,81],[90,39,60]])
total=m.sum(axis=1)
avg=m.mean(axis=1)
for i,(t,a) in enumerate(zip(total,avg),1):
    g='A' if a>=90 else 'B' if a>=80 else 'C' if a>=70 else 'D'
    print(i,t,round(a,2),g)
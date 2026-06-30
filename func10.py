l = [1, 2, 3, 4, 5]
l2=[2,3,4,5,6]
l1 = list(map(lambda x,y:x*y, l,l2))
print(l1) #[1, 4, 9, 16, 25]

l=list(eval(input("Enter 6 subject marks: ")))
l2=[]
res=[]
sum=0
high=l[0]
low=l[0]

for i in l:
    sum=sum+i
    if i>high:
        high=i
    if i<low:
        low=i

per=sum/6

if sum>=540:
    grade="A"
elif sum>=400:
    grade="B"
elif sum>=300:
    grade="C"
else:
    grade="D"

res.append(sum)
res.append(per)
res.append(grade)
res.append(high)
res.append(low)

l2.append("Total")
l2.append("Percentage")
l2.append("Grade")
l2.append("Highest marks")
l2.append("Lowest marks")
print(l2)
print(res)


import pandas as pd
list1=[{'Name':'Sachin','Surname':'Tendulkar'},{'Name':'Mahendra','Surname':'Dhoni'},{'Name':'Rohit','Surname':'Sharma'}]
df1=pd.DataFrame(list1)
for (col_name,col_value) in df1.iteritems():
    print("Column name is: ",col_name)
    print("Column values: ")
    print(col_value)

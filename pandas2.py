import pandas as pd
list1=[{'Name':'Sachin','Surname':'Tendulkar'},{'Name':'Mahendra','Surname':'Dhoni'},{'Name':'Rohit','Surname':'Sharma'}]
df=pd.DataFrame(list1)
for (row_index,row_value) in df.iterrows():
    print("Row index is: ",row_index)
    print("Row values: ")
    print(row_value)

import pymysql

con = None
cursor = None

try:
    con = pymysql.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    def inner_join():
        query="select employee.emp_id,employee.job,dept.dept_id from employee inner join dept on employee.emp_id=dept.dept_id"
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)
        con.commit()
    def left_join():
        query="select employee.ename,employee.salary,dept.dept_name from employee left join dept on employee.emp_id=dept.dept_id"
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)
        con.commit()
    def right_join():
        query="select employee.ename,employee.experience,dept.dept_name from employee right join dept on employee.emp_id=dept.dept_id"
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)
        con.commit()
    def full_join():
        query="select employee.ename,employee.salary,dept.dept_name from employee left join dept on employee.emp_id=dept.dept_id union select employee.ename,employee.experience,dept.dept_name from employee right join dept on employee.emp_id=dept.dept_id"
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)
        con.commit()
    while True:
        print("1.Inner join")
        print("2.Left join")
        print("3.Right join")
        print("4.Full join")
        print("5.Exit")
        ch=int(input("Enter choice: "))
        if ch==1:
            inner_join()
        elif ch==2:
            left_join()
        elif ch==3:
            right_join()
        elif ch==4:
            full_join()
        elif ch==5:
            con.close()
            print("Connection closed")
            break
        else:
            print("Invalid choice")
        
except pymysql.databaseError as e:
    print(e)
finally:
    if cursor:
        cursor.close()
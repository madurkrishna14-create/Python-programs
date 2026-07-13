import pymysql

con = None
cursor = None

try:
    con = pymysql.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    def create():
        query="create table employee(emp_id int(3),ename varchar(20),job varchar(20),experience int(3),salary int(6))"
        cursor.execute(query)
        con.commit()
        print("Table created")
    def insert():
        emp_id=int(input("Enter employee id: "))
        ename=input("Enter employee name: ")
        job=input("Enter job: ")
        experience=int(input("Enter experience in years: "))
        salary=int(input("Enter salary: "))
        query="insert into employee values(%d,'%s','%s',%d,%d)"
        cursor.execute(query%(emp_id,ename,job,experience,salary))
        con.commit()
        print("Record inserted successfully")
    def update():
        emp_id=int(input("Enter employee id to update: "))
        newemp_id=int(input("Enter updated id: "))
        salary=int(input("Enter updated salary: "))
        experience=int(input("Enter updated experience: "))
        query="update employee set emp_id=%d,salary=%d,experience=%d where emp_id=%d"
        cursor.execute(query%(newemp_id,salary,experience,emp_id))
        con.commit()
        print("Record updated successfully")
    def delete():
        emp_id=int(input("Enter employee id to delete: "))
        query="delete from employee where emp_id=%d"
        cursor.execute(query%(emp_id))
        con.commit()
        print("Record deleted successfully")
    def display():
        cursor.execute("select *from employee")
        data=cursor.fetchall()
        for i in data:
            print(i)
    while True:
        print("1.Create table")
        print("2.Insert")
        print("3.Update")
        print("4.Delete")
        print("5.Display")
        print("6.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            create()
        elif ch==2:
            insert()
        elif ch==3:
            update()
        elif ch==4:
            delete()
        elif ch==5:
            display()
        elif ch==6:
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
    
import pymysql

con = None
cursor = None

try:
    con = pymysql.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    def count():
        cursor.execute("select count(emp_id) from employee")
        data=cursor.fetchall()
        for i in data:
            print("Employees: ",list(i))
    def summ():
        cursor.execute("select sum(salary) from employee")
        data=cursor.fetchall()
        for i in data:
            print("Sum of salaries: ",list(i))
    def maxx():
        cursor.execute("select max(salary) from employee")
        data=cursor.fetchall()
        for i in data:
            print("Highest salary: ",list(i))
    def minn():
        cursor.execute("select min(salary) from employee")
        data=cursor.fetchall()
        for i in data:
            print("Lowest salary: ",list(i))
    def avg():
        cursor.execute("select avg(salary) from employee")
        data=cursor.fetchall()
        for i in data:
            print("Average: ",list(i))
    count()
    summ()
    maxx()
    minn()
    avg()
    con.commit()
except pymysql.DatabaseError as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
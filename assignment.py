#student,test,fees table and display data using rollno
import pymysql

con = None
cursor = None

try:
    con = pymysql.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    def create_student():
        query="create table student(rollno int primary key, name varchar(20), branch varchar(20), college varchar(20))"
        cursor.execute(query)
        con.commit()
        print("Student table created")
    def create_test():
        query="create table test(rollno int, m1 int, m2 int, m3 int, m4 int, m5 int, foreign key (rollno) references student(rollno))"
        cursor.execute(query)
        con.commit()
        print("Test table created")
    def create_fees():
        query="create table fees(roll int, fees_paid decimal(10,2), date date,foreign key (roll) references student(rollno))"
        cursor.execute(query)
        con.commit()
        print("Test table created")
    def insert_student():
        cursor.execute("insert into student values(1,'krishna','IT','GPS')")
        cursor.execute("insert into student values(2,'ram','CS','WIT')")
        cursor.execute("insert into student values(3,'sanskar','IT','GPS')")
        cursor.execute("insert into student values(4,'pranav','ME','SWP')")
        cursor.execute("insert into student values(5,'chetan','CE','Sveri')")
        con.commit()
    def insert_test():
        cursor.execute("insert into test values(1,60,70,79,80,78)")
        cursor.execute("insert into test values(2,65,78,90,83,95)")
        cursor.execute("insert into test values(3,89,67,89,64,90)")
        cursor.execute("insert into test values(4,60,88,99,66,91)")
        cursor.execute("insert into test values(5,79,41,56,77,71)")
        con.commit()
    def insert_fees():
        cursor.execute("insert into fees values(1,50000,'2026-01-10')")
        cursor.execute("insert into fees values(2,52000,'2026-02-15')")
        cursor.execute("insert into fees values(3,48000,'2026-03-12')")
        cursor.execute("insert into fees values(4,35000,'2026-03-20')")
        cursor.execute("insert into fees values(5,36000,'2026-03-18')")
        con.commit()
    def display():
        roll=int(input("Enter roll no: "))
        query="SELECT student.rollno,student.name,student.branch, student.college,test.m1,test.m2,test.m3,test.m4,test.m5,fees.fees_paid,fees.date FROM student JOIN test ON student.rollno=test.rollno JOIN fees ON student.rollno=fees.roll WHERE student.rollno=%s"
        cursor.execute(query,(roll,))
        data=cursor.fetchone()
        for i in data:
            print(i,end=" ")
    while True:
        print("\n1.Create tables")
        print("2.Insert data")
        print("3.Display")
        print("4.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            create_student()
            create_test()
            create_fees()
        elif ch==2:
            insert_student()
            insert_test()
            insert_fees()
        elif ch==3:
            display()
        elif ch==4:
            con.close()
            print("Connection closed")
            break
        else:
            print("Invalid choice")
except pymysql.DatabaseError as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    
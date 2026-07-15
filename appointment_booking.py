import pymysql

con = None
cursor = None

try:
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="college"
    )
    cursor = con.cursor()
    print("Connected Successfully")
    while True:
        print("1.Create tables")
        print("2.Add patient")
        print("3.Add doctor")
        print("4.Book appointment")
        print("5.Update appointment")
        print("6.Display appointments")
        print("7.Cancel appointment")
        print("8.Exit")
        ch=int(input("Enter your choice: "))

        if ch==1:
            cursor.execute("create table patients(pid int primary key, name varchar(20), age int, illness varchar(20))")
            cursor.execute("create table doctors(did int primary key,dname varchar(20), status varchar(10))")
            cursor.execute("create table appointments(aid int primary key,pid int,did int ,time varchar(10),foreign key (pid) references patients(pid), foreign key (did) references doctors(did))")
            con.commit()

        elif ch==2:
            pid=int(input("Enter patient id: "))
            name=input("Enter name: ")
            age=int(input("Enter age: "))
            illness=input("Enter illness: ")
            query="insert into patients values(%d,'%s',%d,'%s')"
            cursor.execute(query%(pid,name,age,illness))
            print("Record inserted successfully")
            con.commit()
        elif ch==3:
            did=int(input("Enter doctor id: "))
            dname=input("Enter name: ")
            status=input("Enter status (Available/Occupied): ")
            query="insert into doctors values(%d,'%s','%s')"
            cursor.execute(query%(did,dname,status))
            print("Record inserted successfully")
            con.commit()
        elif ch==4:
            aid=int(input("Enter appointment id: "))
            pid=int(input("Enter patient's id: "))
            did=int(input("Enter doctor's id: "))
            time=input("Enter time: ")
            query="insert into appointments values(%d,%d,%d,'%s')"
            cursor.execute(query%(aid,pid,did,time))
            print("Appointment booked successfully")
            con.commit()
        elif ch==5:
            aid=int(input("Enter appointment id to update: "))
            pid=int(input("Enter patient's new id: "))
            did=int(input("Enter doctor's new id: "))
            time=input("Enter new time: ")
            query="update appointments set pid=%d,did=%d,time='%s' where aid=%d"
            cursor.execute(query%(pid,did,time,aid))
            print("Appointment updated successfully")
            con.commit()
        elif ch==6:
            aid=int(input("Enter appointment id to see details: "))
            query="SELECT patients.pid,patients.name,patients.age,patients.illness,doctors.did,doctors.dname,doctors.status,appointments.aid,appointments.time FROM appointments JOIN patients ON appointments.pid = patients.pid JOIN doctors ON appointments.did = doctors.did WHERE appointments.aid = %s;"
            cursor.execute(query%(aid))
            data=cursor.fetchall()
            for i in data:
                print("Patient id: ",i[0])
                print("Name: ",i[1])
                print("Age: ",i[2])
                print("Illness: ",i[3])
                print("Doctor id: ",i[4])
                print("Doctor name: ",i[5])
                print("Status: ",i[6])
                print("Appointment id: ",i[7])
                print("Time: ",i[8])

        elif ch==7:
            aid=int(input("Enter appointment id to cancel: "))
            query="delete from appointments where aid=%d"
            cursor.execute(query%(aid))
            print("Appointment cancelled successfully")
            con.commit()
        elif ch==8:
            print("Thank you")
            con.close()
            break
        else:
            print("Invalid choice")
            break

except pymysql.DatabaseError as e:
    print("Database Error :", e)

finally:
    if cursor:
        cursor.close()
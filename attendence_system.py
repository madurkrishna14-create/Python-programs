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
    def create_tables():

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            rollno INT PRIMARY KEY,
            name VARCHAR(50),
            class VARCHAR(20)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            aid INT PRIMARY KEY,
            rollno INT,
            att_date DATE,
            status VARCHAR(10),
            FOREIGN KEY(rollno) REFERENCES students(rollno)
        )
        """)

        con.commit()
        print("Tables Created Successfully")
    def insert_student():

        roll = int(input("Enter Roll No: "))
        name = input("Enter Student Name: ")
        cls = input("Enter Class: ")

        query = "INSERT INTO students VALUES(%s,%s,%s)"
        cursor.execute(query, (roll, name, cls))
        con.commit()

        print("Student Added Successfully")
    def mark_attendance():

        aid = int(input("Enter Attendance ID: "))
        roll = int(input("Enter Roll No: "))
        date = input("Enter Date (YYYY-MM-DD): ")
        status = input("Enter Status (Present/Absent): ")

        query = "INSERT INTO attendance VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (aid, roll, date, status))
        con.commit()

        print("Attendance Marked Successfully")
    def update_attendance():

        aid = int(input("Enter Attendance ID: "))
        status = input("Enter New Status (Present/Absent): ")

        query = "UPDATE attendance SET status=%s WHERE aid=%s"
        cursor.execute(query, (status, aid))
        con.commit()

        print("Attendance Updated Successfully")
    def view_report():

        roll = int(input("Enter Roll No: "))

        query = """
        SELECT students.rollno,
               students.name,
               students.class,
               attendance.att_date,
               attendance.status
        FROM students
        JOIN attendance
        ON students.rollno = attendance.rollno
        WHERE students.rollno=%s
        """

        cursor.execute(query, (roll,))
        data = cursor.fetchall()

        if data:
            print("\nATTENDANCE REPORT")
            for row in data:
                print("Roll No :", row[0])
                print("Name    :", row[1])
                print("Class   :", row[2])
                print("Date    :", row[3])
                print("Status  :", row[4])
        else:
            print("No Record Found")
    def display_all():

        query = """
        SELECT students.rollno,
               students.name,
               students.class,
               attendance.att_date,
               attendance.status
        FROM students
        JOIN attendance
        ON students.rollno = attendance.rollno
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nALL ATTENDANCE RECORDS")
            print("-" * 60)
            for row in data:
                print(row)
        else:
            print("No Records Found")
    while True:

        print("\n====== SCHOOL ATTENDANCE MANAGEMENT ======")
        print("1. Create Tables")
        print("2. Insert Student")
        print("3. Mark Attendance")
        print("4. Update Attendance")
        print("5. View Student Attendance Report")
        print("6. Display All Records")
        print("7. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            insert_student()

        elif ch == 3:
            mark_attendance()

        elif ch == 4:
            update_attendance()

        elif ch == 5:
            view_report()

        elif ch == 6:
            display_all()

        elif ch == 7:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

except Exception as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Connection Closed")
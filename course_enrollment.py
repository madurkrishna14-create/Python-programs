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
        CREATE TABLE IF NOT EXISTS course_master(
            cid INT PRIMARY KEY,
            course_name VARCHAR(50),
            duration VARCHAR(20)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_master(
            sid INT PRIMARY KEY,
            student_name VARCHAR(50),
            branch VARCHAR(30)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS course_enrollments(
            eid INT PRIMARY KEY,
            sid INT,
            cid INT,
            enroll_date DATE,
            FOREIGN KEY(sid) REFERENCES student_master(sid),
            FOREIGN KEY(cid) REFERENCES course_master(cid)
        )
        """)

        con.commit()
        print("Tables Created Successfully")
    def add_course():

        cid = int(input("Enter Course ID: "))
        cname = input("Enter Course Name: ")
        duration = input("Enter Course Duration: ")

        query = """
        INSERT INTO course_master(cid, course_name, duration)
        VALUES(%s,%s,%s)
        """
        cursor.execute(query, (cid, cname, duration))
        con.commit()

        print("Course Added Successfully")

    def add_student():

        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")

        query = """
        INSERT INTO student_master(sid, student_name, branch)
        VALUES(%s,%s,%s)
        """
        cursor.execute(query, (sid, name, branch))
        con.commit()

        print("Student Added Successfully")
    def enroll_student():

        eid = int(input("Enter Enrollment ID: "))
        sid = int(input("Enter Student ID: "))
        cid = int(input("Enter Course ID: "))
        date = input("Enter Enrollment Date (YYYY-MM-DD): ")

        query = """
        INSERT INTO course_enrollments(eid, sid, cid, enroll_date)
        VALUES(%s,%s,%s,%s)
        """
        cursor.execute(query, (eid, sid, cid, date))
        con.commit()

        print("Student Enrolled Successfully")

    def unenroll_student():

        eid = int(input("Enter Enrollment ID: "))

        query = "DELETE FROM course_enrollments WHERE eid=%s"
        cursor.execute(query, (eid,))
        con.commit()

        print("Student Unenrolled Successfully")
    def view_enrollments():

        query = """
        SELECT student_master.student_name,
               student_master.branch,
               course_master.course_name,
               course_enrollments.enroll_date
        FROM course_enrollments
        JOIN student_master
        ON course_enrollments.sid = student_master.sid
        JOIN course_master
        ON course_enrollments.cid = course_master.cid
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nENROLLMENT DETAILS")
            for row in data:
                print("Student :", row[0])
                print("Branch  :", row[1])
                print("Course  :", row[2])
                print("Date    :", row[3])
        else:
            print("No Enrollment Records Found")

    while True:

        print("\n====== COURSE ENROLLMENT SYSTEM ======")
        print("1. Create Tables")
        print("2. Add Course")
        print("3. Add Student")
        print("4. Enroll Student")
        print("5. Unenroll Student")
        print("6. View Enrollments")
        print("7. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            add_course()

        elif ch == 3:
            add_student()

        elif ch == 4:
            enroll_student()

        elif ch == 5:
            unenroll_student()

        elif ch == 6:
            view_enrollments()

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
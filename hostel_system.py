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

    # ---------------- CREATE TABLES ----------------
    def create():
        query1 = """
        CREATE TABLE IF NOT EXISTS rooms(
            room_no INT PRIMARY KEY,
            capacity INT,
            occupied INT DEFAULT 0,
            status VARCHAR(20)
        )
        """

        query2 = """
        CREATE TABLE IF NOT EXISTS students1(
            rollno INT PRIMARY KEY,
            name VARCHAR(50),
            branch VARCHAR(30),
            room_no INT,
            FOREIGN KEY(room_no) REFERENCES rooms(room_no)
        )
        """

        cursor.execute(query1)
        cursor.execute(query2)
        con.commit()
        print("Tables Created Successfully")

    # ---------------- ADD ROOM ----------------
    def add_room():
        room = int(input("Enter Room Number : "))
        cap = int(input("Enter Capacity : "))

        query = "INSERT INTO rooms VALUES(%s,%s,0,'Available')"

        cursor.execute(query, (room, cap))
        con.commit()
        print("Room Added Successfully")

    # ---------------- ADD STUDENT ----------------
    def add_student():
        roll = int(input("Enter Roll No : "))
        name = input("Enter Name : ")
        branch = input("Enter Branch : ")

        query = "INSERT INTO students1 VALUES(%s,%s,%s,NULL)"

        cursor.execute(query, (roll, name, branch))
        con.commit()
        print("Student Added Successfully")

    # ---------------- ALLOCATE ROOM ----------------
    def allocate():

        roll = int(input("Enter Student Roll No : "))
        room = int(input("Enter Room Number : "))
        cursor.execute(f"SELECT occupied,capacity FROM rooms WHERE room_no={room}")
        data = cursor.fetchone()

        if data is None:
            print("Room Not Found")
            return

        occupied = data[0]
        capacity = data[1]

        if occupied >= capacity:
            print("Room is Full")
            return

        query = "UPDATE students1 SET room_no=%s WHERE rollno=%s"
        cursor.execute(query, (room, roll))

        query = "UPDATE rooms SET occupied=occupied+1 WHERE room_no=%s"
        cursor.execute(query, (room,))

        query = """
        UPDATE rooms
        SET status='Full'
        WHERE room_no=%s
        AND occupied=capacity
        """
        cursor.execute(query, (room,))

        con.commit()
        print("Room Allocated Successfully")

    # ---------------- VACATE ROOM ----------------
    def vacate():

        roll = int(input("Enter Student Roll No : "))

        query = "SELECT room_no FROM students1 WHERE rollno=%s"
        cursor.execute(query, (roll,))
        data = cursor.fetchone()

        if data is None:
            print("Student Not Found")
            return

        room = data[0]

        if room is None:
            print("Student has no room allocated")
            return

        query = "UPDATE students1 SET room_no=NULL WHERE rollno=%s"
        cursor.execute(query, (roll,))

        query = "UPDATE rooms SET occupied=occupied-1 WHERE room_no=%s"
        cursor.execute(query, (room,))

        query = "UPDATE rooms SET status='Available' WHERE room_no=%s"
        cursor.execute(query, (room,))

        con.commit()
        print("Room Vacated Successfully")

    # ---------------- DISPLAY STUDENTS ----------------
    def display_students():

        query = "SELECT * FROM students1"

        cursor.execute(query)

        data = cursor.fetchall()

        print("\nStudents")
        print("-----------------------------------------------")

        for row in data:
            print(row)

    # ---------------- DISPLAY ROOMS ----------------
    def display_rooms():

        query = "SELECT * FROM rooms"

        cursor.execute(query)

        data = cursor.fetchall()

        print("\nRooms")
        print("-----------------------------------------------")

        for row in data:
            print(row)

    # ---------------- DISPLAY JOIN ----------------
    def display():

        query = """
        SELECT students1.rollno,
               students1.name,
               students1.branch,
               rooms.room_no,
               rooms.capacity,
               rooms.occupied,
               rooms.status
        FROM students1
        LEFT JOIN rooms
        ON students1.room_no=rooms.room_no
        """

        cursor.execute(query)

        data = cursor.fetchall()

        print("\nStudent Room Details")
        print("------------------------------------------------------------")

        for row in data:
            print(row)

    # ---------------- MENU ----------------
    while True:

        print("\n====== HOSTEL ROOM ALLOCATION ======")
        print("1. Create Tables")
        print("2. Add Room")
        print("3. Add Student")
        print("4. Allocate Room")
        print("5. Vacate Room")
        print("6. Display Students")
        print("7. Display Rooms")
        print("8. Display Student-Room Details")
        print("9. Exit")

        ch = int(input("Enter Choice : "))

        if ch == 1:
            create()

        elif ch == 2:
            add_room()

        elif ch == 3:
            add_student()

        elif ch == 4:
            allocate()

        elif ch == 5:
            vacate()

        elif ch == 6:
            display_students()

        elif ch == 7:
            display_rooms()

        elif ch == 8:
            display()

        elif ch == 9:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

except pymysql.MySQLError as e:
    print("Database Error :", e)

finally:
    if cursor:
        cursor.close()

    if con:
        con.close()
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

    def create_tables():

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms_hotel(
            room_no INT PRIMARY KEY,
            room_type VARCHAR(20),
            rent INT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            cid INT PRIMARY KEY,
            customer_name VARCHAR(50),
            phone VARCHAR(15)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            bid INT PRIMARY KEY,
            cid INT,
            room_no INT,
            check_in DATE,
            check_out DATE,
            FOREIGN KEY(cid) REFERENCES customers(cid),
            FOREIGN KEY(room_no) REFERENCES rooms_hotel(room_no)
        )
        """)

        con.commit()
        print("Tables Created Successfully")

    # ---------------- ADD ROOM ----------------

    def add_room():

        room = int(input("Enter Room Number: "))
        rtype = input("Enter Room Type: ")
        rent = int(input("Enter Room Rent: "))

        query = "INSERT INTO rooms_hotel VALUES(%s,%s,%s)"
        cursor.execute(query, (room, rtype, rent))
        con.commit()

        print("Room Added Successfully")

    # ---------------- ADD CUSTOMER ----------------

    def add_customer():

        cid = int(input("Enter Customer ID: "))
        name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")

        query = "INSERT INTO customers VALUES(%s,%s,%s)"
        cursor.execute(query, (cid, name, phone))
        con.commit()

        print("Customer Added Successfully")

    # ---------------- BOOK ROOM ----------------

    def book_room():

        bid = int(input("Enter Booking ID: "))
        cid = int(input("Enter Customer ID: "))
        room = int(input("Enter Room Number: "))
        cin = input("Enter Check-In Date (YYYY-MM-DD): ")
        cout = input("Enter Check-Out Date (YYYY-MM-DD): ")

        query = "INSERT INTO bookings VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query, (bid, cid, room, cin, cout))
        con.commit()

        print("Room Booked Successfully")

    # ---------------- UPDATE BOOKING ----------------

    def update_booking():

        bid = int(input("Enter Booking ID: "))
        cout = input("Enter New Check-Out Date (YYYY-MM-DD): ")

        query = "UPDATE bookings SET check_out=%s WHERE bid=%s"
        cursor.execute(query, (cout, bid))
        con.commit()

        print("Booking Updated Successfully")

    # ---------------- DELETE BOOKING ----------------

    def delete_booking():

        bid = int(input("Enter Booking ID: "))

        query = "DELETE FROM bookings WHERE bid=%s"
        cursor.execute(query, (bid,))
        con.commit()

        print("Booking Deleted Successfully")

    # ---------------- CHECK AVAILABLE ROOMS ----------------

    def available_rooms():

        query = """
        SELECT *
        FROM rooms_hotel
        WHERE room_no NOT IN
        (
            SELECT room_no FROM bookings
        )
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nAVAILABLE ROOMS")
            print("-" * 50)
            for row in data:
                print(row)
        else:
            print("No Rooms Available")

    # ---------------- MENU ----------------

    while True:

        print("\n====== HOTEL ROOM BOOKING SYSTEM ======")
        print("1. Create Tables")
        print("2. Add Room")
        print("3. Add Customer")
        print("4. Book Room")
        print("5. Update Booking")
        print("6. Delete Booking")
        print("7. Check Available Rooms")
        print("8. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            add_room()

        elif ch == 3:
            add_customer()

        elif ch == 4:
            book_room()

        elif ch == 5:
            update_booking()

        elif ch == 6:
            delete_booking()

        elif ch == 7:
            available_rooms()

        elif ch == 8:
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
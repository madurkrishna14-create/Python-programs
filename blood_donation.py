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
        CREATE TABLE IF NOT EXISTS blood_types(
            bid INT PRIMARY KEY,
            blood_group VARCHAR(5)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors(
            did INT PRIMARY KEY,
            donor_name VARCHAR(50),
            phone VARCHAR(15),
            bid INT,
            FOREIGN KEY(bid) REFERENCES blood_types(bid)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests(
            rid INT PRIMARY KEY,
            patient_name VARCHAR(50),
            bid INT,
            request_date DATE,
            FOREIGN KEY(bid) REFERENCES blood_types(bid)
        )
        """)

        con.commit()
        print("Tables Created Successfully")
    def insert_blood_type():

        bid = int(input("Enter Blood Type ID: "))
        group = input("Enter Blood Group (A+, O+, B-, etc.): ")

        query = "INSERT INTO blood_types VALUES(%s,%s)"
        cursor.execute(query, (bid, group))
        con.commit()

        print("Blood Type Added Successfully")

    def register_donor():

        did = int(input("Enter Donor ID: "))
        name = input("Enter Donor Name: ")
        phone = input("Enter Phone Number: ")
        bid = int(input("Enter Blood Type ID: "))

        query = "INSERT INTO donors VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (did, name, phone, bid))
        con.commit()

        print("Donor Registered Successfully")
    def add_request():

        rid = int(input("Enter Request ID: "))
        patient = input("Enter Patient Name: ")
        bid = int(input("Enter Required Blood Type ID: "))
        date = input("Enter Request Date (YYYY-MM-DD): ")

        query = "INSERT INTO requests VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (rid, patient, bid, date))
        con.commit()

        print("Blood Request Added Successfully")
    def view_matching_donors():

        group = input("Enter Blood Group: ")

        query = """
        SELECT donors.did,
               donors.donor_name,
               donors.phone,
               blood_types.blood_group
        FROM donors
        JOIN blood_types
        ON donors.bid = blood_types.bid
        WHERE blood_types.blood_group=%s
        """

        cursor.execute(query, (group,))
        data = cursor.fetchall()

        if data:
            print("\nMATCHING DONORS")
            for row in data:
                print("Donor ID   :", row[0])
                print("Name       :", row[1])
                print("Phone      :", row[2])
                print("Blood Group:", row[3])
        else:
            print("No Matching Donors Found")
    def display_all():

        query = """
        SELECT donors.did,
               donors.donor_name,
               donors.phone,
               blood_types.blood_group
        FROM donors
        JOIN blood_types
        ON donors.bid = blood_types.bid
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nALL DONORS")
            for row in data:
                print(row)
        else:
            print("No Records Found")

    while True:

        print("\n====== BLOOD DONATION SYSTEM ======")
        print("1. Create Tables")
        print("2. Add Blood Type")
        print("3. Register Donor")
        print("4. Add Blood Request")
        print("5. View Matching Donors")
        print("6. Display All Donors")
        print("7. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            insert_blood_type()

        elif ch == 3:
            register_donor()

        elif ch == 4:
            add_request()

        elif ch == 5:
            view_matching_donors()

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
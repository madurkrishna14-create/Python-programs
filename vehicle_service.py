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
        CREATE TABLE IF NOT EXISTS owners(
            oid INT PRIMARY KEY,
            owner_name VARCHAR(50),
            phone VARCHAR(15)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles(
            vid INT PRIMARY KEY,
            vehicle_name VARCHAR(50),
            model VARCHAR(30),
            oid INT,
            FOREIGN KEY(oid) REFERENCES owners(oid)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS service_records(
            sid INT PRIMARY KEY,
            vid INT,
            service_date DATE,
            service_type VARCHAR(50),
            cost INT,
            FOREIGN KEY(vid) REFERENCES vehicles(vid)
        )
        """)

        con.commit()
        print("All Tables Created Successfully")

    def insert_owner():
        oid = int(input("Enter Owner ID: "))
        name = input("Enter Owner Name: ")
        phone = input("Enter Phone Number: ")

        query = "INSERT INTO owners VALUES(%s,%s,%s)"
        cursor.execute(query, (oid, name, phone))
        con.commit()

        print("Owner Added Successfully")

    def insert_vehicle():
        vid = int(input("Enter Vehicle ID: "))
        vname = input("Enter Vehicle Name: ")
        model = input("Enter Model: ")
        oid = int(input("Enter Owner ID: "))

        query = "INSERT INTO vehicles VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (vid, vname, model, oid))
        con.commit()
        print("Vehicle Added Successfully")

    def add_service():
        sid = int(input("Enter Service ID: "))
        vid = int(input("Enter Vehicle ID: "))
        date = input("Enter Service Date (YYYY-MM-DD): ")
        stype = input("Enter Service Type: ")
        cost = int(input("Enter Cost: "))

        query = "INSERT INTO service_records VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query, (sid, vid, date, stype, cost))
        con.commit()
        print("Service Record Added")

    def view_history():
        vid = int(input("Enter Vehicle ID: "))

        query = """
        SELECT owners.owner_name,
               vehicles.vehicle_name,
               vehicles.model,
               service_records.service_date,
               service_records.service_type,
               service_records.cost
        FROM owners
        JOIN vehicles
        ON owners.oid = vehicles.oid
        JOIN service_records
        ON vehicles.vid = service_records.vid
        WHERE vehicles.vid=%s
        """

        cursor.execute(query, (vid,))
        data = cursor.fetchall()

        if data:
            print("\nSERVICE HISTORY")
            for row in data:
                print("Owner Name   :", row[0])
                print("Vehicle Name :", row[1])
                print("Model        :", row[2])
                print("Service Date :", row[3])
                print("Service Type :", row[4])
                print("Cost         :", row[5])

        else:
            print("No Records Found")

    def display_all():

        query = """
        SELECT owners.owner_name,
               vehicles.vehicle_name,
               vehicles.model,
               service_records.service_date,
               service_records.service_type,
               service_records.cost
        FROM owners
        JOIN vehicles
        ON owners.oid=vehicles.oid
        JOIN service_records
        ON vehicles.vid=service_records.vid
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nALL VEHICLE SERVICE RECORDS: ")
            for row in data:
                print(row)
        else:
            print("No Records Found")

    while True:

        print("\n====== VEHICLE SERVICE TRACKER ======")
        print("1. Create Tables")
        print("2. Insert Owner")
        print("3. Insert Vehicle")
        print("4. Add Service Record")
        print("5. View Vehicle Service History")
        print("6. Display All Records")
        print("7. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            insert_owner()

        elif ch == 3:
            insert_vehicle()

        elif ch == 4:
            add_service()

        elif ch == 5:
            view_history()

        elif ch == 6:
            display_all()

        elif ch == 7:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

except pymysql.DatabaseError as e:
    print("Error:",e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Connection Closed")
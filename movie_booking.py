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
        CREATE TABLE IF NOT EXISTS movies(
            mid INT PRIMARY KEY,
            movie_name VARCHAR(50),
            language VARCHAR(20)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS shows(
            sid INT PRIMARY KEY,
            mid INT,
            show_time VARCHAR(20),
            FOREIGN KEY(mid) REFERENCES movies(mid)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movie_bookings(
            bid INT PRIMARY KEY,
            sid INT,
            customer_name VARCHAR(50),
            seats INT,
            FOREIGN KEY(sid) REFERENCES shows(sid)
        )
        """)

        con.commit()
        print("Tables Created Successfully")
    def add_movie():

        mid = int(input("Enter Movie ID: "))
        name = input("Enter Movie Name: ")
        lang = input("Enter Language: ")

        query = """
        INSERT INTO movies(mid, movie_name, language)
        VALUES(%s,%s,%s)
        """
        cursor.execute(query, (mid, name, lang))
        con.commit()

        print("Movie Added Successfully")
    def add_show():

        sid = int(input("Enter Show ID: "))
        mid = int(input("Enter Movie ID: "))
        time = input("Enter Show Time (e.g. 10:00 AM): ")

        query = """
        INSERT INTO shows(sid, mid, show_time)
        VALUES(%s,%s,%s)
        """
        cursor.execute(query, (sid, mid, time))
        con.commit()

        print("Show Added Successfully")
    def book_ticket():

        bid = int(input("Enter Booking ID: "))
        sid = int(input("Enter Show ID: "))
        cname = input("Enter Customer Name: ")
        seats = int(input("Enter Number of Seats: "))

        query = """
        INSERT INTO movie_bookings(bid, sid, customer_name, seats)
        VALUES(%s,%s,%s,%s)
        """
        cursor.execute(query, (bid, sid, cname, seats))
        con.commit()

        print("Ticket Booked Successfully")
    def view_shows():

        query = """
        SELECT movies.movie_name,
               movies.language,
               shows.sid,
               shows.show_time
        FROM movies
        JOIN shows
        ON movies.mid = shows.mid
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nAVAILABLE SHOWS")
            print("-" * 60)
            for row in data:
                print("Movie     :", row[0])
                print("Language  :", row[1])
                print("Show ID   :", row[2])
                print("Show Time :", row[3])
                print("-" * 60)
        else:
            print("No Shows Available")

    def display_bookings():

        query = """
        SELECT movie_bookings.bid,
               movie_bookings.customer_name,
               movies.movie_name,
               shows.show_time,
               movie_bookings.seats
        FROM movie_bookings
        JOIN shows
        ON movie_bookings.sid = shows.sid
        JOIN movies
        ON shows.mid = movies.mid
        """

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            print("\nBOOKING DETAILS")
            for row in data:
                print(row)
        else:
            print("No Bookings Found")
    while True:

        print("\n====== ONLINE MOVIE TICKET BOOKING ======")
        print("1. Create Tables")
        print("2. Add Movie")
        print("3. Add Show")
        print("4. View Shows")
        print("5. Book Ticket")
        print("6. Display Bookings")
        print("7. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_tables()

        elif ch == 2:
            add_movie()

        elif ch == 3:
            add_show()

        elif ch == 4:
            view_shows()

        elif ch == 5:
            book_ticket()

        elif ch == 6:
            display_bookings()

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
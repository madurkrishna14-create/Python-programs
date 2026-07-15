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

    print("Connected Successfully")

    cursor = con.cursor()
    def create():
        query = """
        CREATE TABLE IF NOT EXISTS expenses(
            id INT PRIMARY KEY,
            date DATE,
            amount INT,
            category VARCHAR(20)
        )
        """
        cursor.execute(query)
        con.commit()
        print("Expenses table created successfully.")

    def insert():
        exp_id = int(input("Enter Expense ID: "))
        date = input("Enter Date (YYYY-MM-DD): ")
        amount = int(input("Enter Amount: "))
        category = input("Enter Category: ")

        query = "INSERT INTO expenses VALUES(%d,'%s',%d,'%s')"
        cursor.execute(query % (exp_id, date, amount, category))
        con.commit()

        print("Record inserted successfully.")

    def update():
        exp_id = int(input("Enter Expense ID to update: "))
        date = input("Enter New Date (YYYY-MM-DD): ")
        amount = int(input("Enter New Amount: "))
        category = input("Enter New Category: ")

        query = "UPDATE expenses SET date='%s', amount=%d, category='%s' WHERE id=%d"
        cursor.execute(query % (date, amount, category, exp_id))
        con.commit()

        if cursor.rowcount > 0:
            print("Record updated successfully.")
        else:
            print("Expense ID not found.")
    def delete():
        exp_id = int(input("Enter Expense ID to delete: "))

        query = "DELETE FROM expenses WHERE id=%d"
        cursor.execute(query % exp_id)
        con.commit()

        if cursor.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("Expense ID not found.")
    def display():
        cursor.execute("SELECT * FROM expenses")
        data = cursor.fetchall()

        if data:
            print("\nID\tDate\t\tAmount\tCategory")
            print("-" * 40)
            for row in data:
                print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
        else:
            print("No records found.")

    def monthly_summary():

        cursor.execute("SELECT SUM(amount) FROM expenses")
        total = cursor.fetchone()

        cursor.execute("SELECT AVG(amount) FROM expenses")
        avg = cursor.fetchone()

        print("\nMonthly Summary")
        print("----------------")

        if total[0] is None:
            print("Total Expenses : 0")
        else:
            print("Total Expenses :", total[0])

        if avg[0] is None:
            print("Average Expense :", 0)
        else:
            print("Average Expense :", round(avg[0], 2))

    # ---------------- MENU ----------------
    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Create Table")
        print("2. Insert Expense")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Display Expenses")
        print("6. Monthly Summary")
        print("7. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            create()

        elif ch == 2:
            insert()

        elif ch == 3:
            update()

        elif ch == 4:
            delete()

        elif ch == 5:
            display()

        elif ch == 6:
            monthly_summary()

        elif ch == 7:
            print("Connection Closed.")
            con.close()
            break

        else:
            print("Invalid Choice.")

except pymysql.DatabaseError as e:
    print("Database Error:", e)

finally:
    if cursor:
        cursor.close()
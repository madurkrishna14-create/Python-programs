import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute("select * from staff")
    data = cursor.fetchall()

    list1 = []
    for row in data:
        t = (row[0], row[1], row[2])
        list1.append(t)

    print("Final list1:", list1)

except mysql.connector.Error as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
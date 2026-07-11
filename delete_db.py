import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute("delete from games where game_id=201")
    con.commit()
    print("Record deleted successfully")
except mysql.connector.Error as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
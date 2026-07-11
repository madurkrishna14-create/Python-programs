import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute("update games set game_id='201' where game_id='101'")
    cursor.execute("update games set name='Basketball' where name='Football'")
    print("Records updated successfully")

    con.commit()
except mysql.connector.Error as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
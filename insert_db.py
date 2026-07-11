import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    #cursor.execute("create table games (game_id int (2),name varchar(20), type varchar(20))")
    #print("Table created")
    cursor.execute("insert into games values(102,'Football','Outdoor')")
    cursor.execute("insert into games values(103,'Chess','Indoor')")
    cursor.execute("insert into games values(104,'Caroom','Indoor')")
    con.commit()
except mysql.connector.Error as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
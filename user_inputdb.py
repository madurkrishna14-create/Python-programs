import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(host='localhost', database='college', user='root', password='admin')
    print("Connected successfully")

    cursor = con.cursor()
    while True:
        game_id=int(input("Enter game id: "))
        name=input("Enter game name: ")
        type=input("Enter game type(Indoor/Outdoor): ")
        sql="insert into games values(%d,'%s','%s')"
        cursor.execute(sql%(game_id,name,type))
        print("User record inserted successfully")
        option=input("Do you want to insert another record(yes/no): ")
        if option=="no":
            con.commit()
            break
except mysql.connector.Error as e:
    print("There is a problem with sql: ", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
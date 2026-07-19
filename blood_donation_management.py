import pymysql

con = pymysql.connect(host="localhost", user="root", password="admin", database="college")
cursor = con.cursor()

def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS blood_types(
    bid INT PRIMARY KEY,
    blood_group VARCHAR(5))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS donors(
    did INT PRIMARY KEY,
    donor_name VARCHAR(50),
    phone VARCHAR(15),
    bid INT,
    FOREIGN KEY(bid) REFERENCES blood_types(bid))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS requests(
    rid INT PRIMARY KEY,
    patient_name VARCHAR(50),
    bid INT,
    did INT,
    request_date DATE,
    FOREIGN KEY(bid) REFERENCES blood_types(bid),
    FOREIGN KEY(did) REFERENCES donors(did))""")
    con.commit()
    print("Tables Created")
def insert_blood_type():
    cursor.execute("INSERT INTO blood_types VALUES(%s,%s)",
                   (int(input("ID: ")), input("Blood Group: ")))
    con.commit()

def update_blood_type():
    cursor.execute("UPDATE blood_types SET blood_group=%s WHERE bid=%s",
                   (input("New Group: "), int(input("ID: "))))
    con.commit()

def delete_blood_type():
    cursor.execute("DELETE FROM blood_types WHERE bid=%s",(int(input("ID: ")),))
    con.commit()

def display_blood_types():
    cursor.execute("SELECT * FROM blood_types")
    for r in cursor.fetchall():
        print(r)

def insert_donor():
    cursor.execute("INSERT INTO donors VALUES(%s,%s,%s,%s)",
    (int(input("ID: ")),input("Name: "),input("Phone: "),int(input("Blood Type ID: "))))
    con.commit()

def update_donor():
    cursor.execute("UPDATE donors SET donor_name=%s,phone=%s,bid=%s WHERE did=%s",
    (input("Name: "),input("Phone: "),int(input("Blood Type ID: ")),int(input("Donor ID: "))))
    con.commit()

def delete_donor():
    cursor.execute("DELETE FROM donors WHERE did=%s",(int(input("Donor ID: ")),))
    con.commit()

def display_donors():
    cursor.execute("""SELECT d.did,d.donor_name,d.phone,b.blood_group
                   FROM donors d JOIN blood_types b ON d.bid=b.bid""")
    for r in cursor.fetchall(): 
        print(r)

def insert_request():
    cursor.execute("INSERT INTO requests VALUES(%s,%s,%s,%s,%s)",
    (int(input("Request ID: ")),input("Patient: "),int(input("Blood Type ID: ")),
     int(input("Donor ID: ")),input("Date(YYYY-MM-DD): ")))
    con.commit()

def update_request():
    cursor.execute("""UPDATE requests SET patient_name=%s,bid=%s,did=%s,request_date=%s WHERE rid=%s""",
    (input("Patient: "),int(input("Blood Type ID: ")),int(input("Donor ID: ")),
     input("Date: "),int(input("Request ID: "))))
    con.commit()

def delete_request():
    cursor.execute("DELETE FROM requests WHERE rid=%s",(int(input("Request ID: ")),))
    con.commit()

def display_requests():
    cursor.execute("""SELECT r.rid,r.patient_name,b.blood_group,d.donor_name,r.request_date
    FROM requests r JOIN blood_types b ON r.bid=b.bid
    JOIN donors d ON r.did=d.did""")
    for r in cursor.fetchall(): 
        print(r)

def view_matching():
    bg=input("Blood Group: ")
    cursor.execute("""SELECT d.did,d.donor_name,d.phone,b.blood_group
    FROM donors d JOIN blood_types b ON d.bid=b.bid WHERE b.blood_group=%s""",(bg,))
    for r in cursor.fetchall():
        print(r)

while True:
    print("""
1.Create Tables
2.Insert Blood Type
3.Update Blood Type
4.Delete Blood Type
5.Display Blood Types
6.Insert Donor
7.Update Donor
8.Delete Donor
9.Display Donors
10.Insert Request
11.Update Request
12.Delete Request
13.Display Requests
14.View Matching Donors
15.Exit""")
    ch=int(input("Choice: "))
    if ch==1:
        create_tables()
    elif ch==2:
        insert_blood_type()
    elif ch==3:
        update_blood_type()
    elif ch==4:
        delete_blood_type()
    elif ch==5:
        display_blood_types()
    elif ch==6:
        insert_donor()
    elif ch==7:
        update_donor()
    elif ch==8:
        delete_donor()
    elif ch==9:
        display_donors()
    elif ch==10:
        insert_request()
    elif ch==11:
        update_request()
    elif ch==12:
        delete_request()
    elif ch==13:
        display_requests()
    elif ch==14:
        view_matching()
    elif ch==15:
        break
    else: 
        print("Invalid")
cursor.close()
con.close()

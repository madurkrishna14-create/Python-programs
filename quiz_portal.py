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
    def create():
        query1 = """
        CREATE TABLE IF NOT EXISTS users(
            userid INT PRIMARY KEY,
            username VARCHAR(50)
        )
        """
        query2 = """
        CREATE TABLE IF NOT EXISTS questions(
            qid INT PRIMARY KEY,
            question VARCHAR(200),
            option1 VARCHAR(50),
            option2 VARCHAR(50),
            option3 VARCHAR(50),
            option4 VARCHAR(50),
            correct_option INT
        )
        """
        query3 = """
        CREATE TABLE IF NOT EXISTS answers(
            userid INT,
            qid INT,
            selected_option INT,
            result VARCHAR(10),
            PRIMARY KEY(userid,qid),
            FOREIGN KEY(userid) REFERENCES users(userid),
            FOREIGN KEY(qid) REFERENCES questions(qid)
        )
        """
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        con.commit()
        print("Tables Created Successfully")
    def add_user():
        userid = int(input("Enter User ID : "))
        username = input("Enter User Name : ")
        query = "INSERT INTO users VALUES(%s,%s)"
        cursor.execute(query, (userid, username))
        con.commit()
        print("User Added Successfully")

    def add_question():
        qid = int(input("Enter Question ID : "))
        question = input("Enter Question : ")
        op1 = input("Option 1 : ")
        op2 = input("Option 2 : ")
        op3 = input("Option 3 : ")
        op4 = input("Option 4 : ")
        correct = int(input("Correct Option (1-4): "))
        query = """
        INSERT INTO questions
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query, (qid, question, op1, op2, op3, op4, correct))
        con.commit()
        print("Question Added Successfully")

    def view_questions():
        cursor.execute("SELECT * FROM questions")
        data = cursor.fetchall()
        print("\nQuestions: ")
        for row in data:
            print("Question ID :", row[0])
            print("Question :", row[1])
            print("1.", row[2])
            print("2.", row[3])
            print("3.", row[4])
            print("4.", row[5])
            print()

    def take_quiz():
        userid = int(input("Enter User ID : "))
        cursor.execute("SELECT * FROM users WHERE userid=%s", (userid,))
        if cursor.fetchone() is None:
            print("User Not Found")
            return
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
        score = 0
        for q in questions:
            print("\nQuestion ID :", q[0])
            print(q[1])
            print("1.", q[2])
            print("2.", q[3])
            print("3.", q[4])
            print("4.", q[5])
            ans = int(input("Enter Your Answer (1-4): "))
            if ans == q[6]:
                result = "Correct"
                score += 1
            else:
                result = "Wrong"
            query = """
            INSERT INTO answers
            VALUES(%s,%s,%s,%s)
            """
            cursor.execute(query, (userid, q[0], ans, result))
        con.commit()
        print("\nQuiz Completed")
        print("Score :", score, "/", len(questions))

    def score():
        userid = int(input("Enter User ID : "))
        query = """
        SELECT COUNT(*)
        FROM answers
        WHERE userid=%s
        AND result='Correct'
        """
        cursor.execute(query, (userid,))
        marks = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM questions")
        total = cursor.fetchone()[0]
        print("\nFinal Score :", marks, "/", total)

    def users():
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        print("\nUsers: ")
        for row in data:
            print(row)

    def answers():
        query = """
        SELECT users.username,
               questions.question,
               answers.selected_option,
               answers.result
        FROM answers
        JOIN users
        ON users.userid=answers.userid
        JOIN questions
        ON questions.qid=answers.qid
        """
        cursor.execute(query)
        data = cursor.fetchall()
        print("\nQuiz Report: ")
        for row in data:
            print(row)
    while True:
        print("\n========== ONLINE QUIZ PORTAL ==========")
        print("1. Create Tables")
        print("2. Add User")
        print("3. Add Question")
        print("4. View Questions")
        print("5. Take Quiz")
        print("6. View Score")
        print("7. View Users")
        print("8. View Answers")
        print("9. Exit")
        ch = int(input("Enter Choice : "))
        if ch == 1:
            create()
        elif ch == 2:
            add_user()
        elif ch == 3:
            add_question()
        elif ch == 4:
            view_questions()
        elif ch == 5:
            take_quiz()
        elif ch == 6:
            score()
        elif ch == 7:
            users()
        elif ch == 8:
            answers()
        elif ch == 9:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
except pymysql.DatabaseError as e:
    print("Database Error :", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
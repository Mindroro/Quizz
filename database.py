import sqlite3

def start():
    with sqlite3.connect("quizz.db") as connect:
        cursor = connect.cursor()
        sql = "CREATE TABLE IF NOT EXISTS questions_tb (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, right_ans TEXT, false_ans1 TEXT, false_ans2 TEXT, false_ans3 TEXT)"
        cursor.execute(sql)
        connect.commit()

def deltable():
    with sqlite3.connect("quizz.db") as connect:
        cursor = connect.cursor()
        sql = "DROP TABLE questions_tb"
        cursor.execute(sql)
        connect.commit()

def addque(question, right_ans, false_ans1, false_ans2, false_ans3):
    with sqlite3.connect("quizz.db") as connect:
        cursor = connect.cursor()
        sql = "INSERT INTO questions_tb (question, right_ans, false_ans1, false_ans2, false_ans3) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, (question, right_ans, false_ans1, false_ans2, false_ans3))
        connect.commit()

def getall():
    with sqlite3.connect("quizz.db") as connect:
        #connect.row_factory = sqlite3.Row
        cursor = connect.cursor()
        sql = "SELECT * FROM questions_tb"
        res = cursor.execute(sql).fetchall()
        return res
    
def getque():
    '''функція повертае список запитань'''
    with sqlite3.connect("quizz.db") as connect:
        cursor = connect.cursor()
        sql = "SELECT question FROM questions_tb"
        res = cursor.execute(sql).fetchall()
        result = []
        for i in res:
            result.append(i[0])
        return result

#deltable()    
#start()
#addque("a", "b", "c", "d", "e")
#addque("f", "g", "h", "i", "j")

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from database import *
from random import shuffle, choice

app = QApplication([])
from widgetsplay import *
window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Quizz")
window.setLayout(v_line_main)

class Data():
    def __init__(self, row):
        self.question = row[1]
        self.right_ans = row[2]
        self.wrong_ans1 = row[3]
        self.wrong_ans2 = row[4]
        self.wrong_ans3 = row[5]

    def __repr__(self):
        return f"Data {self.question}"

everything = getall()
datalist = []
for row in everything:
    datalist.append(Data(row))

rightanscount = 0
questionscount = len(datalist)

buttonlist = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def quetowidgets(dataq: Data):
    lb_question.setText(dataq.question)
    shuffle(buttonlist)
    buttonlist[0].setText(dataq.right_ans)
    buttonlist[1].setText(dataq.wrong_ans1)
    buttonlist[2].setText(dataq.wrong_ans2)
    buttonlist[3].setText(dataq.wrong_ans3)
    lb_right_ans.setText(dataq.right_ans)

def check():
    global rightanscount
    if buttonlist[0].isChecked():
        lb_result.setText("Вірно")
        rightanscount += 1
    else:
        lb_result.setText("Невірно")

def newque():
    if datalist:
        dataq = choice(datalist)
        quetowidgets(dataq)
        datalist.remove(dataq)
    else:
        message = QMessageBox()
        message.setText(f"Ваш результат: {rightanscount}/{questionscount}")
        message.exec_()
        btn_next.setText("закінчіти")

def next():
    if btn_next.text() == "відповісти":
        btn_next.setText("наступне запитання")
        check()
        group_res.show()
        group_ans.hide()
    elif btn_next.text() == "наступне запитання":
        btn_next.setText("відповісти")
        newque()
        btn_group.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        btn_group.setExclusive(True)
        group_res.hide()
        group_ans.show()
    elif btn_next.text() == "закінчіти":
        window.close()

newque()    
btn_next.clicked.connect(next)

window.show()
app.exec_()
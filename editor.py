from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from database import *

app = QApplication([])
from widgetsed import *

window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Editor")
window.setLayout(hline_main)
lw.addItems(getque())

def showvar():
    if lw.selectedItems():
        question = lw.selectedItems()[0].text()
        data = getans(question)
        le_r_ans.setText(data[0])
        le_w_ans1.setText(data[1])
        le_w_ans2.setText(data[2])
        le_w_ans3.setText(data[3])

def createque():
    question, ok = QInputDialog.getText(window, "Нове запитання", "Введіть запитання")
    questions = getque()
    if question not in questions and question != "" and ok == True:
        lw.addItem(question)
        addque(question, "", "", "", "")

def saveque():
    if lw.selectedItems():
        question = lw.selectedItems()[0].text()
        change(
            question=question,
            r_ans=le_r_ans.text(),
            w_ans1=le_w_ans1.text(),
            w_ans2=le_w_ans2.text(),
            w_ans3=le_w_ans3.text()
        )

def delque():
    if lw.selectedItems():
        question = lw.selectedItems()[0].text()
        remque(question)
        lw.clear()
        lw.addItems(getque())
        le_r_ans.clear()
        le_w_ans1.clear()
        le_w_ans2.clear()
        le_w_ans3.clear()

lw.itemClicked.connect(showvar)
btn_create.clicked.connect(createque)
btn_save.clicked.connect(saveque)
btn_remove.clicked.connect(delque)

window.show()
app.exec_()
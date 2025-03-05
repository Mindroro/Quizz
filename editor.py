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
        data =  getans(question)
        le_r_ans.setText(data[0])
        le_w_ans1.setText(data[1])
        le_w_ans2.setText(data[2])
        le_w_ans3.setText(data[3])

lw.itemClicked.connect(showvar)

window.show()
app.exec_()
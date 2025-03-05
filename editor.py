from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from database import *

app = QApplication([])
from widgetsed import *

window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Editor")
window.setLayout(hline_main)
lw.addItems(getque())

window.show()
app.exec_()
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog

app = QApplication([])
from widgetsed import *

window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Editor")
window.setLayout(hline_main)


window.show()
app.exec_()
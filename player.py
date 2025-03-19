from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
from widgetsplay import *
window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Quizz")
window.setLayout(v_line_main)
window.show()
app.exec_()
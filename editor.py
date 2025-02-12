from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog

app = QApplication([])
window = QWidget()
window.resize(700, 400)
window.setWindowTitle("Editor")



window.show()
app.exec_()
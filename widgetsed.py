
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QListWidget, QHBoxLayout, QVBoxLayout

lw = QListWidget()
btn_save = QPushButton("зберегти")
btn_remove = QPushButton("видалити")
btn_create = QPushButton("створити")
lb_r_ans = QLabel("Правильна відповідь:")
le_r_ans = QLineEdit()
lb_w_ans1 = QLabel("Неправильна відповідь")
le_w_ans1 = QLineEdit()
lb_w_ans2 = QLabel("Неправильна відповідь")
le_w_ans2 = QLineEdit()
lb_w_ans3 = QLabel("Неправильна відповідь")
le_w_ans3 = QLineEdit()

hline = QHBoxLayout()
hline.addWidget(btn_create)
hline.addWidget(btn_remove)
hline.addWidget(btn_save)
vline = QVBoxLayout()
vline.addWidget(lb_r_ans, 1)
vline.addWidget(le_r_ans, 1)
vline.addWidget(lb_w_ans1, 1)
vline.addWidget(le_w_ans1, 1)
vline.addWidget(lb_w_ans2, 1)
vline.addWidget(le_w_ans2, 1)
vline.addWidget(lb_w_ans3, 1)
vline.addWidget(le_w_ans3, 1)
vline.addStretch(1)
vline.addLayout(hline)
vline.addStretch(1)
hline_main = QHBoxLayout()
hline_main.addWidget(lw)
hline_main.addLayout(vline)
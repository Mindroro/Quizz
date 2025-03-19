from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox, QButtonGroup
from PyQt5.QtCore import Qt

lb_question = QLabel("2 + 2 = ?")

#Group Box для запитань
btn_group = QButtonGroup()
rbtn_1 = QRadioButton("59")
btn_group.addButton(rbtn_1)
rbtn_2 = QRadioButton("4")
btn_group.addButton(rbtn_2)
rbtn_3 = QRadioButton("33")
btn_group.addButton(rbtn_3)
rbtn_4 = QRadioButton("5")
btn_group.addButton(rbtn_4)

group_ans = QGroupBox()
v_line = QVBoxLayout()
h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_1.addWidget(rbtn_1)
h_line_1.addWidget(rbtn_2)
h_line_2.addWidget(rbtn_3)
h_line_2.addWidget(rbtn_4)
v_line.addLayout(h_line_1)
v_line.addLayout(h_line_2)
group_ans.setLayout(v_line)

#Group Box для результатів
lb_result = QLabel("Вірно")
lb_right_ans = QLabel("4")
v_line_1 = QVBoxLayout()
v_line_1.addWidget(lb_result)
v_line_1.addWidget(lb_right_ans)
group_res = QGroupBox()
group_res.setLayout(v_line_1)

btn_next = QPushButton("відповісти")

v_line_main = QVBoxLayout()
v_line_main.addWidget(lb_question)
v_line_main.addWidget(group_ans)
v_line_main.addWidget(group_res)
v_line_main.addWidget(btn_next)
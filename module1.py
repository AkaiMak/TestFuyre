#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Студент
#
# Created:     22.10.2024
# Copyright:   (c) Студент 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from inspy import *
class MainWin(QWidget):
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
  def initUI(self):
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.button = QPushButton(txt_next)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.hello_text)
    self.layout.addWidget(self.instruction)
    self.layout.addWidget(self.button)
  def connects(self):
    self.btn_next.clicked.connect(self.next_click)
  def next_click(self):
    self.hide()
    self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()





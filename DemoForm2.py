# DemoForm2.py
# DemoForm.ui(화면을 저장) + DemoForm.py(로직을 저장)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self)
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self)
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self)
        self.label.setText("세번째 버튼 클릭")

# 직접 모듈을 실행했는지 체크
if __name__=="__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()

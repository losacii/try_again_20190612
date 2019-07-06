from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.title = "PyQt5 Events"
        self.top = 100
        self.left = 100
        self.width = 960
        self.height = 540

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("./resource/home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.UiComponents()

        self.show()

    def UiComponents(self):

        btn = QPushButton("Click This!", self)
        btn.setGeometry(QRect(100, 30, 150, 40))

        btn1 = QPushButton("Click This!", self)
        btn1.setGeometry(QRect(100, 80, 150, 40))
        btn1.setIcon(QtGui.QIcon("./resource/home.png"))
        btn1.setIconSize(QtCore.QSize(30,30))
        btn1.setToolTip("<h3>This is a button click TIP!</h3>")

        btn2 = QPushButton("Hello World! (exit)", self)
        btn2.setGeometry(QRect(100, 130, 150, 40))
        btn2.clicked.connect(self.hello)

    def hello(self):
        print("Hello World!")
        sys.exit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

"""
    btn.clicked.connect(<function>)
"""

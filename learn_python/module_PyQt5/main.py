from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 960
        self.height = 540

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("./resource/home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

App = QApplication(sys.argv)
print('pyqt5')
window = Window()
sys.exit(App.exec())
print('pyqt5')
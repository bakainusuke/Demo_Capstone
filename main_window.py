from PyQt5 import QtCore, QtGui, QtWidgets
# from ui_main_intro import Ui_MainWindow
from ui_main_layout import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QSettings Demo")

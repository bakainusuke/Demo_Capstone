from PyQt5 import QtCore, QtGui, QtWidgets
from upload_page import Ui_UploadWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main window widgets
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 231, 141))
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(180, 260, 113, 32))
        self.upload.setObjectName("upload")
        self.upload.clicked.connect(self.show_upload_page)

        self.new_ana = QtWidgets.QPushButton(self.centralwidget)
        self.new_ana.setGeometry(QtCore.QRect(340, 260, 113, 32))
        self.new_ana.setObjectName("new_ana")

        self.saved_ana = QtWidgets.QPushButton(self.centralwidget)
        self.saved_ana.setGeometry(QtCore.QRect(520, 260, 113, 32))
        self.saved_ana.setObjectName("saved_ana")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 43))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_upload_page(self):
        # Show upload page widgets
        self.upload_page_widgets = Ui_UploadWindow()
        self.upload_page_widgets.setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Periscope"))
        self.label.setText(_translate("MainWindow", "Periscope"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.new_ana.setText(_translate("MainWindow", "New Analysis"))
        self.saved_ana.setText(_translate("MainWindow", "Saved Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UploadWindow(object):
    def setupUi(self, UploadWindow, main_window):
        self.window = UploadWindow
        self.main_window = main_window

        UploadWindow.setObjectName("UploadWindow")
        UploadWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UploadWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.upload_data = QtWidgets.QPushButton(self.centralwidget)
        self.upload_data.setGeometry(QtCore.QRect(120, 240, 151, 131))
        self.upload_data.setObjectName("upload_data")

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 40, 113, 32))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.show_main_page)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        UploadWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UploadWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 43))
        self.menubar.setObjectName("menubar")
        UploadWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UploadWindow)
        self.statusbar.setObjectName("statusbar")
        UploadWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UploadWindow)
        QtCore.QMetaObject.connectSlotsByName(UploadWindow)

    def show_main_page(self):
        self.main_window.show()
        self.window.hide()

    def retranslateUi(self, UploadWindow):
        _translate = QtCore.QCoreApplication.translate
        UploadWindow.setWindowTitle(_translate("UploadWindow", "MainWindow"))
        self.upload_data.setText(_translate("UploadWindow", "Upload"))
        self.back.setText(_translate("UploadWindow", "Back"))
        self.label.setText(_translate("UploadWindow", "Upload Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UploadWindow = QtWidgets.QMainWindow()
    ui = Ui_UploadWindow()
    ui.setupUi(UploadWindow, None)
    UploadWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from main_window import Ui_MainWindow

class Ui_UploadWindow(object):
    def setupUi(self, UploadWindow):
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
        # self.back.clicked.connect(self.show_main_page)
        
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

    # def show_main_page(self):
    #     # Show upload page widgets
    #     self.upload_page_widgets = Ui_MainWindow()
    #     self.upload_page_widgets.setupUi(UploadWindow)

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
    ui.setupUi(UploadWindow)
    UploadWindow.show()
    sys.exit(app.exec_())

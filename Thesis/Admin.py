# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sstudent_reg1 import Ui_reg
from sstudent_rec import Ui_rec
from sattendance import Ui_at

class ui_admin(object):
        def setupUi(self, admin):
                admin.setObjectName("admin")
                admin.setEnabled(True)
                admin.resize(1366, 768)
                font = QtGui.QFont()
                font.setKerning(True)
                admin.setFont(font)
                admin.setStyleSheet("")
                admin.setAnimated(True)
                self.centralwidget = QtWidgets.QWidget(admin)
                self.centralwidget.setObjectName("centralwidget")
                self.reg = QtWidgets.QPushButton(self.centralwidget)
                self.reg.setGeometry(QtCore.QRect(50, 440, 171, 41))

                self.reg.clicked.connect(self.regwindow)

                font = QtGui.QFont()
                font.setFamily("Sitka")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(True)
                font.setWeight(9)
                self.reg.setFont(font)
                self.reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.reg.setAutoFillBackground(False)
                self.reg.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
                self.reg.setAutoDefault(False)
                self.reg.setDefault(False)
                self.reg.setFlat(False)
                self.reg.setObjectName("reg")
                self.background = QtWidgets.QLabel(self.centralwidget)
                self.background.setGeometry(QtCore.QRect(0, 0, 1366, 768))
                self.background.setText("")
                self.background.setPixmap(QtGui.QPixmap("background/minimalist-4k-wallpaper-hd-15-920x518.jpg"))
                self.background.setScaledContents(True)
                self.background.setObjectName("background")
                self.view_record = QtWidgets.QPushButton(self.centralwidget)
                self.view_record.setGeometry(QtCore.QRect(330, 440, 171, 41))

                self.view_record.clicked.connect(self.recbutton)

                font = QtGui.QFont()
                font.setFamily("Sitka")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(True)
                font.setWeight(9)
                self.view_record.setFont(font)
                self.view_record.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.view_record.setAutoFillBackground(False)
                self.view_record.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
                self.view_record.setAutoDefault(False)
                self.view_record.setDefault(False)
                self.view_record.setFlat(False)
                self.view_record.setObjectName("view_record")
                self.attendance = QtWidgets.QPushButton(self.centralwidget)
                self.attendance.setGeometry(QtCore.QRect(600, 440, 171, 41))

                self.attendance.clicked.connect(self.attendbutton)

                font = QtGui.QFont()
                font.setFamily("Sitka")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(True)
                font.setWeight(9)
                self.attendance.setFont(font)
                self.attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.attendance.setAutoFillBackground(False)
                self.attendance.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
                self.attendance.setAutoDefault(False)
                self.attendance.setDefault(False)
                self.attendance.setFlat(False)
                self.attendance.setObjectName("attendance")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 50, 1366, 311))
                self.label.setAutoFillBackground(True)
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("background/nemco.jpg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.background.raise_()
                self.reg.raise_()
                self.view_record.raise_()
                self.attendance.raise_()
                self.label.raise_()
                admin.setCentralWidget(self.centralwidget)

                self.retranslateUi(admin)
                QtCore.QMetaObject.connectSlotsByName(admin)

        def retranslateUi(self, admin):
                _translate = QtCore.QCoreApplication.translate
                admin.setWindowTitle(_translate("admin", "MainWindow"))
                self.reg.setText(_translate("admin", "Registration"))
                self.view_record.setText(_translate("admin", "View Record"))
                self.attendance.setText(_translate("admin", "Attendance"))
        
        def regbutton(self):
                self.regwindow()
                #print("hello")
                #admin.close()

        def recbutton(self):
                self.recwindow()
                #admin.close()
        
        def attendbutton(self):
                self.attendwindow()
        
        def regwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_reg()
                self.ui.setupUi(self.window)
                self.window.show()

        def recwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_rec()
                self.ui.setupUi(self.window)
                self.window.show()
        def attendwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_at()
                self.ui.setupUi(self.window)
                self.window.show()        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin = QtWidgets.QMainWindow()
    ui = ui_admin()
    ui.setupUi(admin)
    admin.showMaximized()
    sys.exit(app.exec_())

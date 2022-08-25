# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sstudent_reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import sqlite3,sys
import os,csv,cv2
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reg(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.setEnabled(True)
        main.resize(600, 601)
        font = QtGui.QFont()
        font.setKerning(True)
        main.setFont(font)
        main.setStyleSheet("")
        main.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 601))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background/minimalist-4k-wallpaper-hd-15-920x518.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.regframe = QtWidgets.QFrame(self.centralwidget)
        self.regframe.setGeometry(QtCore.QRect(10, 20, 581, 571))
        self.regframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.regframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.regframe.setObjectName("regframe")
        self.vacstatus = QtWidgets.QLabel(self.regframe)
        self.vacstatus.setGeometry(QtCore.QRect(350, 180, 211, 111))
        self.vacstatus.setAutoFillBackground(False)
        self.vacstatus.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.vacstatus.setText("")
        self.vacstatus.setObjectName("vacstatus")
        self.label = QtWidgets.QLabel(self.regframe)
        self.label.setGeometry(QtCore.QRect(0, 0, 581, 571))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background/HD-wallpaper-portrait-display-vertical-pattern-digital-art-cyan-polygon-art.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.addpicstud_4 = QtWidgets.QPushButton(self.regframe)
        self.addpicstud_4.setGeometry(QtCore.QRect(360, 510, 81, 31))
        
        self.addpicstud_4.clicked.connect(self.save)
        
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addpicstud_4.setFont(font)
        self.addpicstud_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addpicstud_4.setAutoFillBackground(False)
        self.addpicstud_4.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.addpicstud_4.setAutoDefault(False)
        self.addpicstud_4.setDefault(False)
        self.addpicstud_4.setFlat(False)
        self.addpicstud_4.setObjectName("addpicstud_4")
        self.stphone = QtWidgets.QLineEdit(self.regframe)
        self.stphone.setGeometry(QtCore.QRect(150, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stphone.setFont(font)
        self.stphone.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stphone.setText("")
        self.stphone.setObjectName("stphone")
        self.stcurse = QtWidgets.QLineEdit(self.regframe)
        self.stcurse.setGeometry(QtCore.QRect(10, 350, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stcurse.setFont(font)
        self.stcurse.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stcurse.setText("")
        self.stcurse.setObjectName("stcurse")
        self.stlastname = QtWidgets.QLineEdit(self.regframe)
        self.stlastname.setGeometry(QtCore.QRect(150, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stlastname.setFont(font)
        self.stlastname.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stlastname.setText("")
        self.stlastname.setObjectName("stlastname")
        self.styear = QtWidgets.QLineEdit(self.regframe)
        self.styear.setGeometry(QtCore.QRect(10, 430, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styear.setFont(font)
        self.styear.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.styear.setText("")
        self.styear.setObjectName("styear")
        self.stextensio = QtWidgets.QLineEdit(self.regframe)
        self.stextensio.setGeometry(QtCore.QRect(150, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stextensio.setFont(font)
        self.stextensio.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stextensio.setText("")
        self.stextensio.setObjectName("stextensio")
        self.stmajor = QtWidgets.QLineEdit(self.regframe)
        self.stmajor.setGeometry(QtCore.QRect(10, 390, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stmajor.setFont(font)
        self.stmajor.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stmajor.setText("")
        self.stmajor.setObjectName("stmajor")
        self.addpicstud_3 = QtWidgets.QPushButton(self.regframe)
        self.addpicstud_3.setGeometry(QtCore.QRect(470, 510, 81, 31))
        
        self.addpicstud_3.clicked.connect(self.cancell)
        
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addpicstud_3.setFont(font)
        self.addpicstud_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addpicstud_3.setAutoFillBackground(False)
        self.addpicstud_3.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.addpicstud_3.setAutoDefault(False)
        self.addpicstud_3.setDefault(False)
        self.addpicstud_3.setFlat(False)
        self.addpicstud_3.setObjectName("addpicstud_3")
        self.label_6 = QtWidgets.QLabel(self.regframe)
        self.label_6.setGeometry(QtCore.QRect(350, 100, 175, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color:rgb(85, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.stfirstname = QtWidgets.QLineEdit(self.regframe)
        self.stfirstname.setGeometry(QtCore.QRect(150, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stfirstname.setFont(font)
        self.stfirstname.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stfirstname.setText("")
        self.stfirstname.setObjectName("stfirstname")
        self.stmiddle = QtWidgets.QLineEdit(self.regframe)
        self.stmiddle.setGeometry(QtCore.QRect(150, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stmiddle.setFont(font)
        self.stmiddle.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.stmiddle.setText("")
        self.stmiddle.setObjectName("stmiddle")
        self.label_2 = QtWidgets.QLabel(self.regframe)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 351, 111))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 87 16pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.studentid = QtWidgets.QLineEdit(self.regframe)
        self.studentid.setGeometry(QtCore.QRect(150, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.studentid.setFont(font)
        self.studentid.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.studentid.setText("")
        self.studentid.setObjectName("studentid")
        self.studpic = QtWidgets.QLabel(self.regframe)
        self.studpic.setGeometry(QtCore.QRect(20, 100, 111, 111))
        self.studpic.setAutoFillBackground(False)
        self.studpic.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.studpic.setText("")
        self.studpic.setObjectName("studpic")
        self.addpicstud = QtWidgets.QPushButton(self.regframe)
        self.addpicstud.setGeometry(QtCore.QRect(30, 220, 81, 31))
        
        self.addpicstud.clicked.connect(self.take)
        
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addpicstud.setFont(font)
        self.addpicstud.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addpicstud.setAutoFillBackground(False)
        self.addpicstud.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.addpicstud.setAutoDefault(False)
        self.addpicstud.setDefault(False)
        self.addpicstud.setFlat(False)
        self.addpicstud.setObjectName("addpicstud")
        self.addpicstud_2 = QtWidgets.QPushButton(self.regframe)
        self.addpicstud_2.setGeometry(QtCore.QRect(410, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.addpicstud_2.setFont(font)
        self.addpicstud_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addpicstud_2.setAutoFillBackground(False)
        self.addpicstud_2.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.addpicstud_2.setAutoDefault(False)
        self.addpicstud_2.setDefault(False)
        self.addpicstud_2.setFlat(False)
        self.addpicstud_2.setObjectName("addpicstud_2")
        self.loginlogo = QtWidgets.QLabel(self.regframe)
        self.loginlogo.setGeometry(QtCore.QRect(50, 20, 71, 71))
        self.loginlogo.setAutoFillBackground(False)
        self.loginlogo.setText("")
        self.loginlogo.setPixmap(QtGui.QPixmap("background/nemco_logo1.jpg"))
        self.loginlogo.setScaledContents(True)
        self.loginlogo.setWordWrap(False)
        self.loginlogo.setObjectName("loginlogo")
        self.comboBox = QtWidgets.QComboBox(self.regframe)
        self.comboBox.setGeometry(QtCore.QRect(350, 140, 211, 31))
        self.comboBox.setStyleSheet("font: 12pt \"Sitka\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label.raise_()
        self.addpicstud_4.raise_()
        self.stphone.raise_()
        self.stcurse.raise_()
        self.stlastname.raise_()
        self.styear.raise_()
        self.stextensio.raise_()
        self.stmajor.raise_()
        self.addpicstud_3.raise_()
        self.label_6.raise_()
        self.stfirstname.raise_()
        self.stmiddle.raise_()
        self.label_2.raise_()
        self.studentid.raise_()
        self.studpic.raise_()
        self.addpicstud.raise_()
        self.addpicstud_2.raise_()
        self.vacstatus.raise_()
        self.loginlogo.raise_()
        self.comboBox.raise_()
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.addpicstud_4.setText(_translate("main", "SAVE"))
        self.stphone.setPlaceholderText(_translate("main", "Phone Number"))
        self.stcurse.setPlaceholderText(_translate("main", "Course"))
        self.stlastname.setPlaceholderText(_translate("main", "Last Name"))
        self.styear.setPlaceholderText(_translate("main", "Year level - Section"))
        self.stextensio.setPlaceholderText(_translate("main", "Extension"))
        self.stmajor.setPlaceholderText(_translate("main", "Major"))
        self.addpicstud_3.setText(_translate("main", "CANCEL"))
        self.label_6.setText(_translate("main", "Vaccination Status"))
        self.stfirstname.setPlaceholderText(_translate("main", "First Name"))
        self.stmiddle.setPlaceholderText(_translate("main", "Middle Name"))
        self.label_2.setText(_translate("main", "STUDENTS REGISTRATION"))
        self.studentid.setPlaceholderText(_translate("main", "Student ID"))
        self.addpicstud.setText(_translate("main", "Add Picture"))
        self.addpicstud_2.setText(_translate("main", "Add Picture"))
        self.comboBox.setItemText(0, _translate("main", "Fully Vaccinated with Booster"))
        self.comboBox.setItemText(1, _translate("main", "Fully Vaccinated"))
        self.comboBox.setItemText(2, _translate("main", "1st Dose Only"))
        self.comboBox.setItemText(3, _translate("main", "Unvaccinated"))
    
    def cancell(self):
        main.close()
        
    def save(self):
        idnum = self.studentid.text()
        fname1 = self.stfirstname.text()
        lastname1 = self.stlastname.text()
        phonenumber = self.stphone.text()
        vacstatus = self.comboBox.currentText()
        
        if len(idnum)!= 0 and len(fname1)!=0 and len(lastname1)!= 0 and len(phonenumber)!=0 and len(vacstatus)!=0:    
            
            self.add_register()
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("WARNING")
            msg.setText("Invalid Input")
            x = msg.exec()
    
    def take(self):
        idnum = self.studentid.text()
        fname1 = self.stfirstname.text()
        
        if len(idnum)!= 0 and len(fname1)!=0:    
            
            self.TakeImages()
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("WARNING")
            msg.setText("Invalid Input")
            x = msg.exec()
        
        
        
    def ok(self):
        msg = QMessageBox()
        msg.setWindowTitle("Notice")
        msg.setText("Student Added")
        x = msg.exec()
        
    def connection(self):
        try:
            conn = sqlite3.connect("manage.db")
        except:
            print("cannot connect to the database")
        return conn

    def add_register(self):
        conn = self.connection()
        cur = conn.cursor()
        
        stid = self.studentid.text()
        lname = self.stlastname.text()
        fname = self.stfirstname.text()
        mname = self.stmiddle.text()
        ext = self.stextensio.text()
        phone = self.stphone.text()
        cour = self.stcurse.text()
        stat = self.comboBox.currentText()
        maj = self.stmajor.text()
        yrsec =self.styear.text()

        cur.execute("CREATE TABLE IF NOT EXISTS Management (Student_ID INTEGER NOT NULL, Last_Name TEXT NOT NULL, First_Name TEXT NOT NULL, Middle_Name TEXT NOT NULL, Extension TEXT, Phone_Number INTEGER NOT NULL, Course TEXT NOT NULL, Status TEXT NOT NULL, Major TEXT, Year_And_Section TEXT NOT NULL)")
        sql = "INSERT INTO  Management (Student_ID, Last_Name, First_Name, Middle_Name, Extension, Phone_Number, Course, Status, Major, Year_And_Section ) VALUES (?,?,?,?,?,?,?,?,?,?)"
        val = (stid, lname, fname, mname, ext, phone, cour, stat, maj, yrsec)

        cur.execute(sql, val)
        conn.commit()
        conn.close()
        
        self.ok()
        
    def TakeImages(self):
       
         #Initialize the classifier
        faceCascade = cv2.CascadeClassifier("/home/admin/Desktop/Thesis_UI/New_UI/Thesis/haarcascades/haarcascade_frontalface_default.xml")

            # Start the video camera
        vc = cv2.VideoCapture(0)

            # Get the userId and userName
            #print("Enter the id and name of the person: ")
            
        userId = self.studentid.text()
        userName = self.stfirstname.text()
            
            #userId = input()
            #userName = input()

            # Initially Count is = 1
        count = 1
        num_of_images = 0

            # Function to save the image
        def saveImage(image, userName, userId, imgId):
                # Save the images inside the previously created folder
            cv2.imwrite("/home/admin/Desktop/Thesis_UI/New_UI/Thesis/dataset/{}.jpeg".format(userId), image)
            print("[INFO] Image {} has been saved  : {}".format(imgId, userName))

        print("[INFO] Video Capture is now starting please stay still...")

        while True:
                # Capture the frame/image
            ret, img = vc.read()

                # Copy the original Image
            originalImg = img.copy()

                # Get the gray version of our image
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Get the coordinates of the location of the face in the picture
            faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

                # Draw a rectangle at the location of the coordinates
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                coords = [x, y, w, h]
                
                # Show the image
                #cv2.imshow("Identified Face", img)
            cv2.imshow("Press Space to take a photo", img)
                
                
                    # Wait for user keypress
            key = cv2.waitKey(20)
                #rawCapture.truncate(0)
                # Check if the pressed key is 'k' or 'q'
            if key == ord('s'): #or count > 4:
                break
            elif key == 32:
                try:
                    roi_img = originalImg[coords[1]: coords[1] + coords[3], coords[0]: coords[0] + coords[2]]
                    saveImage(roi_img, userName, userId, count)
                    count += 1

                except:
                    pass
                
                    # If count is less than 5 then save the image
                    # If q is pressed break out of the loop
            #print("[INFO] Dataset has been created for {}".format(userName))
        # Stop the video camera
        vc.release()
            # Close all Windows
        cv2.destroyAllWindows()
        self.studpic.setScaledContents(True)
        pixmap = QPixmap('/home/admin/Desktop/Thesis_UI/New_UI/Thesis/dataset/'+ userId +'.jpeg')
        self.studpic.setPixmap(pixmap)
        self.studpic.repaint()
        
   
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_reg()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())


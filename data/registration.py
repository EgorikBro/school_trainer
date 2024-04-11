from PyQt5 import QtCore, QtGui, QtWidgets


class RegistrationUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 421)
        Form.setMinimumSize(QtCore.QSize(617, 421))
        Form.setMaximumSize(QtCore.QSize(617, 421))
        Form.setStyleSheet("background-color: #43766C")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 601, 101))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 15pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(10, 120, 601, 71))
        self.messageLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                             "font: 10pt \"MS Sans Serif\";\n"
                                             "color: #F8FAE5;\n"
                                             "font-weight: 600;\n"
                                             "padding: 5px 15px;\n"
                                             "margin-top: 0px;\n"
                                             "outline: 0px;")
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 241, 31))
        self.label_3.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.loginEdit = QtWidgets.QLineEdit(Form)
        self.loginEdit.setGeometry(QtCore.QRect(270, 210, 331, 31))
        self.loginEdit.setStyleSheet("background-color: #F8FAE5;\n"
                                     "font: 13pt \"MS Sans Serif\";\n"
                                     "color: #B19470;\n"
                                     "font-weight: 600;\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid #B19470;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;\n"
                                     "hover: { background-color: red };\n"
                                     "pressed: { background-color: rgb(0, 255, 0)}")
        self.loginEdit.setText("")
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Form)
        self.passwordEdit.setGeometry(QtCore.QRect(270, 250, 331, 31))
        self.passwordEdit.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 13pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;\n"
                                        "hover: { background-color: red };\n"
                                        "pressed: { background-color: rgb(0, 255, 0)}")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit2 = QtWidgets.QLineEdit(Form)
        self.passwordEdit2.setGeometry(QtCore.QRect(270, 290, 331, 31))
        self.passwordEdit2.setStyleSheet("background-color: #F8FAE5;\n"
                                         "font: 13pt \"MS Sans Serif\";\n"
                                         "color: #B19470;\n"
                                         "font-weight: 600;\n"
                                         "border-radius: 8px;\n"
                                         "border: 2px solid #B19470;\n"
                                         "margin-top: 0px;\n"
                                         "outline: 0px;\n"
                                         "hover: { background-color: red };\n"
                                         "pressed: { background-color: rgb(0, 255, 0)}")
        self.passwordEdit2.setText("")
        self.passwordEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit2.setObjectName("passwordEdit2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 241, 31))
        self.label_4.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 241, 31))
        self.label_5.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.createBtn = QtWidgets.QPushButton(Form)
        self.createBtn.setGeometry(QtCore.QRect(10, 360, 591, 41))
        self.createBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                     "font: 13pt \"MS Sans Serif\";\n"
                                     "color: #B19470;\n"
                                     "font-weight: 600;\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid #B19470;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;\n"
                                     "hover: { background-color: red };\n"
                                     "pressed: { background-color: rgb(0, 255, 0)}")
        self.createBtn.setObjectName("createBtn")
        self.showPassBtn = QtWidgets.QCheckBox(Form)
        self.showPassBtn.setGeometry(QtCore.QRect(390, 330, 181, 20))
        self.showPassBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                       "font: 10pt \"MS Sans Serif\";\n"
                                       "color: #F8FAE5;\n"
                                       "font-weight: 600;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;")
        self.showPassBtn.setObjectName("showPassBtn")
        self.studentBtn = QtWidgets.QRadioButton(Form)
        self.studentBtn.setGeometry(QtCore.QRect(20, 330, 121, 20))
        self.studentBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #F8FAE5;\n"
                                      "font-weight: 600;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.studentBtn.setChecked(True)
        self.studentBtn.setObjectName("studentBtn")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.studentBtn)
        self.teacherBtn = QtWidgets.QRadioButton(Form)
        self.teacherBtn.setGeometry(QtCore.QRect(150, 330, 131, 20))
        self.teacherBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #F8FAE5;\n"
                                      "font-weight: 600;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.teacherBtn.setObjectName("teacherBtn")
        self.buttonGroup_2.addButton(self.teacherBtn)
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.backBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #B19470;\n"
                                   "font-weight: 600;\n"
                                   "border-radius: 8px;\n"
                                   "border: 2px solid #B19470;\n"
                                   "padding: 5px 15px;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;\n"
                                   "hover: { background-color: red };\n"
                                   "pressed: { background-color: rgb(0, 255, 0)}")
        self.backBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/icon6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_3.setText(_translate("Form", "Логин:"))
        self.label_4.setText(_translate("Form", "Повторите пароль:"))
        self.label_5.setText(_translate("Form", "Пароль:"))
        self.createBtn.setText(_translate("Form", "Создать аккаунт"))
        self.showPassBtn.setText(_translate("Form", "Показать пароль"))
        self.studentBtn.setText(_translate("Form", "Ученик"))
        self.teacherBtn.setText(_translate("Form", "Учитель"))

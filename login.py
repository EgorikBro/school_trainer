from PyQt5 import QtCore, QtGui, QtWidgets


class LoginUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(442, 320)
        Form.setMinimumSize(QtCore.QSize(442, 320))
        Form.setMaximumSize(QtCore.QSize(442, 320))
        Form.setStyleSheet("background-color: #43766C")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(10, 90, 421, 40))
        self.messageLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                        "font: 10pt \"MS Sans Serif\";\n"
                                        "color: #F8FAE5;\n"
                                        "font-weight: 600;\n"
                                        "padding: 5px 15px;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;")
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 82, 29))
        self.label_3.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(11, 194, 99, 29))
        self.label_4.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.loginEdit = QtWidgets.QLineEdit(Form)
        self.loginEdit.setGeometry(QtCore.QRect(120, 150, 311, 31))
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
        self.passwordEdit.setGeometry(QtCore.QRect(120, 190, 311, 31))
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
        self.passwordEdit.setText("")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.entranceBtn = QtWidgets.QPushButton(Form)
        self.entranceBtn.setGeometry(QtCore.QRect(10, 260, 421, 43))
        self.entranceBtn.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.entranceBtn.setObjectName("entranceBtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(11, 30, 421, 40))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 15pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.showPassBtn = QtWidgets.QCheckBox(Form)
        self.showPassBtn.setGeometry(QtCore.QRect(250, 230, 181, 20))
        self.showPassBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                       "font: 10pt \"MS Sans Serif\";\n"
                                       "color: #F8FAE5;\n"
                                       "font-weight: 600;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;")
        self.showPassBtn.setObjectName("showPassBtn")
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
        icon.addPixmap(QtGui.QPixmap("ui\\../pictures/icon6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Логин:"))
        self.label_4.setText(_translate("Form", "Пароль:"))
        self.entranceBtn.setText(_translate("Form", "Войти"))
        self.label.setText(_translate("Form", "Вход"))
        self.showPassBtn.setText(_translate("Form", "Показать пароль"))

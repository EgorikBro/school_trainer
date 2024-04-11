from PyQt5 import QtCore, QtGui, QtWidgets


class ProfileEditUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 494)
        Form.setMinimumSize(QtCore.QSize(469, 494))
        Form.setMaximumSize(QtCore.QSize(469, 494))
        Form.setStyleSheet("background-color: #43766C")
        self.avatarLabel = QtWidgets.QLabel(Form)
        self.avatarLabel.setGeometry(QtCore.QRect(180, 10, 121, 121))
        self.avatarLabel.setText("")
        self.avatarLabel.setPixmap(QtGui.QPixmap("data/avatars/default_icon.png"))
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setObjectName("avatarLabel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 220, 101, 31))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.acceptBtn = QtWidgets.QPushButton(Form)
        self.acceptBtn.setGeometry(QtCore.QRect(10, 450, 451, 31))
        self.acceptBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                     "font: 10pt \"MS Sans Serif\";\n"
                                     "color: #B19470;\n"
                                     "font-weight: 600;\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid #B19470;\n"
                                     "padding: 5px 15px;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;\n"
                                     "hover: { background-color: red };\n"
                                     "pressed: { background-color: rgb(0, 255, 0)}")
        self.acceptBtn.setObjectName("acceptBtn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 101, 31))
        self.label_2.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_2.setObjectName("label_2")
        self.nameEdit = QtWidgets.QLineEdit(Form)
        self.nameEdit.setGeometry(QtCore.QRect(120, 221, 341, 31))
        self.nameEdit.setStyleSheet("background-color: #F8FAE5;\n"
                                    "font: 10pt \"MS Sans Serif\";\n"
                                    "color: #B19470;\n"
                                    "font-weight: 600;\n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid #B19470;\n"
                                    "margin-top: 0px;\n"
                                    "outline: 0px;\n"
                                    "hover: { background-color: red };\n"
                                    "pressed: { background-color: rgb(0, 255, 0)}")
        self.nameEdit.setObjectName("nameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Form)
        self.passwordEdit.setGeometry(QtCore.QRect(120, 261, 341, 31))
        self.passwordEdit.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 10pt \"MS Sans Serif\";\n"
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
        self.showPassBtn = QtWidgets.QCheckBox(Form)
        self.showPassBtn.setGeometry(QtCore.QRect(280, 310, 181, 20))
        self.showPassBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                       "font: 10pt \"MS Sans Serif\";\n"
                                       "color: #F8FAE5;\n"
                                       "font-weight: 600;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;")
        self.showPassBtn.setObjectName("showPassBtn")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(10, 140, 451, 61))
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
        self.avatarBtn = QtWidgets.QPushButton(Form)
        self.avatarBtn.setGeometry(QtCore.QRect(180, 10, 121, 121))
        self.avatarBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.avatarBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                     "font: 10pt \"MS Sans Serif\";\n"
                                     "color: #F8FAE5;\n"
                                     "font-weight: 600;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;")
        self.avatarBtn.setText("")
        self.avatarBtn.setFlat(True)
        self.avatarBtn.setObjectName("avatarBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Имя:"))
        self.acceptBtn.setText(_translate("Form", "Сохранить изменения"))
        self.label_2.setText(_translate("Form", "Пароль:"))
        self.showPassBtn.setText(_translate("Form", "Показать пароль"))

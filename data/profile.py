from PyQt5 import QtCore, QtGui, QtWidgets


class ProfileUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 499)
        Form.setMinimumSize(QtCore.QSize(467, 499))
        Form.setMaximumSize(QtCore.QSize(467, 499))
        Form.setStyleSheet("background-color: #43766C")
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
        self.avatarLabel = QtWidgets.QLabel(Form)
        self.avatarLabel.setGeometry(QtCore.QRect(180, 10, 121, 121))
        self.avatarLabel.setText("")
        self.avatarLabel.setPixmap(QtGui.QPixmap("data/avatars/default_icon.png"))
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setObjectName("avatarLabel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 180, 91, 31))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setGeometry(QtCore.QRect(110, 180, 351, 31))
        self.nameLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                     "font: 13pt \"MS Sans Serif\";\n"
                                     "color: #F8FAE5;\n"
                                     "font-weight: 600;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;")
        self.nameLabel.setText("")
        self.nameLabel.setScaledContents(True)
        self.nameLabel.setObjectName("nameLabel")
        self.editAccBtn = QtWidgets.QPushButton(Form)
        self.editAccBtn.setGeometry(QtCore.QRect(10, 410, 451, 31))
        self.editAccBtn.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.editAccBtn.setObjectName("editAccBtn")
        self.changeAccBtn = QtWidgets.QPushButton(Form)
        self.changeAccBtn.setGeometry(QtCore.QRect(10, 450, 451, 31))
        self.changeAccBtn.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.changeAccBtn.setObjectName("changeAccBtn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.label_3.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_3.setObjectName("label_3")
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(110, 220, 351, 31))
        self.statusLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                       "font: 13pt \"MS Sans Serif\";\n"
                                       "color: #F8FAE5;\n"
                                       "font-weight: 600;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;")
        self.statusLabel.setText("")
        self.statusLabel.setScaledContents(True)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Имя:"))
        self.editAccBtn.setText(_translate("Form", "Редактировать профиль"))
        self.changeAccBtn.setText(_translate("Form", "Сменить аккаунт"))
        self.label_3.setText(_translate("Form", "Статус:"))

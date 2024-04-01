from PyQt5 import QtCore, QtGui, QtWidgets


class MyTestsUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(834, 707)
        Form.setMinimumSize(QtCore.QSize(834, 707))
        Form.setMaximumSize(QtCore.QSize(834, 707))
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
        icon.addPixmap(QtGui.QPixmap("ui\\../pictures/icon6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setObjectName("backBtn")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 70, 791, 541))
        self.listView.setStyleSheet("background-color: #F8FAE5;\n"
                                    "font: 13pt \"MS Sans Serif\";\n"
                                    "color: #B19470;\n"
                                    "font-weight: 600;\n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid #B19470;\n"
                                    "margin-top: 0px;\n"
                                    "outline: 0px;")
        self.listView.setObjectName("listView")
        self.createBtn = QtWidgets.QPushButton(Form)
        self.createBtn.setGeometry(QtCore.QRect(20, 640, 791, 41))
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
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(70, 10, 741, 51))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.createBtn.setText(_translate("Form", "Создать тест"))

from PyQt5 import QtCore, QtGui, QtWidgets


class EntranceUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(325, 282)
        Form.setMinimumSize(QtCore.QSize(325, 282))
        Form.setMaximumSize(QtCore.QSize(325, 282))
        Form.setStyleSheet("background-color: #43766C")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 111, 51))
        self.pushButton.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 120, 181, 51))
        self.pushButton_2.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Войти"))
        self.pushButton_2.setText(_translate("Form", "Создать аккаунт"))

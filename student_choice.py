from PyQt5 import QtCore, QtGui, QtWidgets


class StudentChoiceUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
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
        self.exampleBtn = QtWidgets.QPushButton(Form)
        self.exampleBtn.setGeometry(QtCore.QRect(100, 70, 211, 41))
        self.exampleBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.exampleBtn.setObjectName("exampleBtn")
        self.myTestsBtn = QtWidgets.QPushButton(Form)
        self.myTestsBtn.setGeometry(QtCore.QRect(100, 130, 211, 41))
        self.myTestsBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.myTestsBtn.setObjectName("myTestsBtn")
        self.teachersTestBtn = QtWidgets.QPushButton(Form)
        self.teachersTestBtn.setGeometry(QtCore.QRect(100, 190, 211, 41))
        self.teachersTestBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                           "font: 13pt \"MS Sans Serif\";\n"
                                           "color: #B19470;\n"
                                           "font-weight: 600;\n"
                                           "border-radius: 8px;\n"
                                           "border: 2px solid #B19470;\n"
                                           "margin-top: 0px;\n"
                                           "outline: 0px;\n"
                                           "hover: { background-color: red };\n"
                                           "pressed: { background-color: rgb(0, 255, 0)}")
        self.teachersTestBtn.setObjectName("teachersTestBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exampleBtn.setText(_translate("Form", "Пример теста"))
        self.myTestsBtn.setText(_translate("Form", "Мои тесты"))
        self.teachersTestBtn.setText(_translate("Form", "Тест от учителя"))

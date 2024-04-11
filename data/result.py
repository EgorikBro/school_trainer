from PyQt5 import QtCore, QtGui, QtWidgets


class ResultUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 458)
        Form.setMinimumSize(QtCore.QSize(518, 458))
        Form.setMaximumSize(QtCore.QSize(518, 458))
        Form.setStyleSheet("background-color: #43766C")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 290, 300, 31))
        self.label.setStyleSheet("background-color: #D3D3D3;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #808080;\n"
                                 "font-weight: 600;\n"
                                 "border-radius: 8px;\n"
                                 "border: 2px solid #000000;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.scale = QtWidgets.QLabel(Form)
        self.scale.setGeometry(QtCore.QRect(110, 290, 16, 31))
        self.scale.setStyleSheet("background-color: #008000;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #808080;\n"
                                 "font-weight: 600;\n"
                                 "border-radius: 8px;\n"
                                 "border: 2px solid #000000;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.scale.setText("")
        self.scale.setObjectName("scale")
        self.percent = QtWidgets.QLabel(Form)
        self.percent.setGeometry(QtCore.QRect(190, 280, 141, 51))
        self.percent.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 16pt \"MS Sans Serif\";\n"
                                   "color: #000000;\n"
                                   "font-weight: 600;\n"
                                   "padding: 5px 15px;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.percent.setAlignment(QtCore.Qt.AlignCenter)
        self.percent.setObjectName("percent")
        self.rightLabel = QtWidgets.QLabel(Form)
        self.rightLabel.setGeometry(QtCore.QRect(10, 180, 501, 41))
        self.rightLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #EEEEEE;\n"
                                      "font-weight: 600;\n"
                                      "padding: 5px 15px;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.rightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightLabel.setObjectName("rightLabel")
        self.gradeLabel = QtWidgets.QLabel(Form)
        self.gradeLabel.setGeometry(QtCore.QRect(10, 230, 501, 41))
        self.gradeLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #EEEEEE;\n"
                                      "font-weight: 600;\n"
                                      "padding: 5px 15px;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.gradeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gradeLabel.setObjectName("gradeLabel")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 501, 81))
        self.label_4.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 18pt \"MS Sans Serif\";\n"
                                   "color: #EEEEEE;\n"
                                   "font-weight: 600;\n"
                                   "padding: 5px 15px;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.continueBtn = QtWidgets.QPushButton(Form)
        self.continueBtn.setGeometry(QtCore.QRect(450, 390, 51, 51))
        self.continueBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                       "font: 13pt \"MS Sans Serif\";\n"
                                       "color: #B19470;\n"
                                       "font-weight: 600;\n"
                                       "border-radius: 8px;\n"
                                       "border: 2px solid #000000;\n"
                                       "padding: 5px 15px;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;\n"
                                       "hover: { background-color: red };\n"
                                       "pressed: { background-color: rgb(0, 255, 0)}")
        self.continueBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/pictures/icon8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.continueBtn.setIcon(icon)
        self.continueBtn.setIconSize(QtCore.QSize(40, 40))
        self.continueBtn.setObjectName("continueBtn")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 390, 261, 51))
        self.pushButton.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #000000;\n"
                                      "padding: 5px 15px;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.percent.setText(_translate("Form", "0%"))
        self.rightLabel.setText(_translate("Form", "Выполнено верно: "))
        self.gradeLabel.setText(_translate("Form", "Ваша оценка - "))
        self.label_4.setText(_translate("Form", "Вы прошли тест!"))
        self.pushButton.setText(_translate("Form", "Показать ответы"))

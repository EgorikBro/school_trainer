from PyQt5 import QtCore, QtGui, QtWidgets


class CreateTestStudentUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 423)
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
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 130, 401, 41))
        self.lineEdit.setStyleSheet("background-color: #F8FAE5;\n"
                                    "font: 13pt \"MS Sans Serif\";\n"
                                    "color: #B19470;\n"
                                    "font-weight: 600;\n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid #B19470;\n"
                                    "margin-top: 0px;\n"
                                    "outline: 0px;\n"
                                    "hover: { background-color: red };\n"
                                    "pressed: { background-color: rgb(0, 255, 0)}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 130, 131, 41))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setObjectName("label")
        self.createBtn = QtWidgets.QPushButton(Form)
        self.createBtn.setGeometry(QtCore.QRect(10, 370, 541, 41))
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
        self.messageLabel.setGeometry(QtCore.QRect(70, 20, 471, 91))
        self.messageLabel.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                        "font: 13pt;\n"
                                        "color: #8B0000;\n"
                                        "font-weight: 600;\n"
                                        "padding: 5px 15px;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;")
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 190, 531, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                       "font: 13pt \"MS Sans Serif\";\n"
                                       "color: #F8FAE5;\n"
                                       "font-weight: 600;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                         "font: 13pt \"MS Sans Serif\";\n"
                                         "color: #F8FAE5;\n"
                                         "font-weight: 600;\n"
                                         "margin-top: 0px;\n"
                                         "outline: 0px;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                         "font: 13pt \"MS Sans Serif\";\n"
                                         "color: #F8FAE5;\n"
                                         "font-weight: 600;\n"
                                         "margin-top: 0px;\n"
                                         "outline: 0px;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                         "font: 13pt \"MS Sans Serif\";\n"
                                         "color: #F8FAE5;\n"
                                         "font-weight: 600;\n"
                                         "margin-top: 0px;\n"
                                         "outline: 0px;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название:"))
        self.createBtn.setText(_translate("Form", "Создать тест"))
        self.radioButton.setText(_translate("Form", "Сопоставление термин-определение"))
        self.radioButton_2.setText(_translate("Form", "Написание определения"))
        self.radioButton_3.setText(_translate("Form", "Тест с вариантами ответа"))
        self.radioButton_4.setText(_translate("Form", "Сопоставление с картинками"))

from PyQt5 import QtCore, QtGui, QtWidgets


class FinishUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 302)
        Form.setStyleSheet("background-color: #43766C")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 381, 41))
        self.pushButton.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 15, 381, 41))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 15pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 90, 371, 101))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Завершить"))
        self.label.setText(_translate("Form", "Последний штрих"))
        self.radioButton.setText(_translate("Form", "термин -> определение"))
        self.radioButton_2.setText(_translate("Form", "определение -> термин"))

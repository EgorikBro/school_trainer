from PyQt5 import QtCore, QtGui, QtWidgets


class TestEditorUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 707)
        Form.setStyleSheet("background-color: #43766C")
        self.questionText = QtWidgets.QTextEdit(Form)
        self.questionText.setGeometry(QtCore.QRect(230, 40, 481, 141))
        self.questionText.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 13pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;\n"
                                        "hover: { background-color: red };\n"
                                        "pressed: { background-color: rgb(0, 255, 0)}")
        self.questionText.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.questionText.setReadOnly(False)
        self.questionText.setObjectName("questionText")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 240, 661, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_4.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.textEdit_4.setReadOnly(False)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 3, 1, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_1.setText("")
        self.radioButton_1.setObjectName("radioButton_1")
        self.buttonGroup.addButton(self.radioButton_1)
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.textEdit_3.setReadOnly(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.gridLayout.addWidget(self.radioButton_4, 3, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.textEdit_1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_1.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.textEdit_1.setReadOnly(False)
        self.textEdit_1.setObjectName("textEdit_1")
        self.gridLayout.addWidget(self.textEdit_1, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 13pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;\n"
                                      "hover: { background-color: red };\n"
                                      "pressed: { background-color: rgb(0, 255, 0)}")
        self.textEdit_2.setReadOnly(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
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
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(10, 190, 911, 41))
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 650, 361, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 650, 271, 41))
        self.pushButton_2.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 13pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
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
        self.questionText.setHtml(_translate("Form",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_1.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Завершить создание теста"))
        self.pushButton_2.setText(_translate("Form", "Добавить вопрос"))

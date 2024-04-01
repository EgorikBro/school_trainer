from PyQt5 import QtCore, QtGui, QtWidgets


class DefinitionUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(717, 573)
        Form.setMinimumSize(QtCore.QSize(717, 573))
        Form.setMaximumSize(QtCore.QSize(717, 573))
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
        self.continueBtn = QtWidgets.QPushButton(Form)
        self.continueBtn.setGeometry(QtCore.QRect(10, 520, 211, 41))
        self.continueBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                       "font: 13pt \"MS Sans Serif\";\n"
                                       "color: #B19470;\n"
                                       "font-weight: 600;\n"
                                       "border-radius: 8px;\n"
                                       "border: 2px solid #B19470;\n"
                                       "margin-top: 0px;\n"
                                       "outline: 0px;\n"
                                       "hover: { background-color: red };\n"
                                       "pressed: { background-color: rgb(0, 255, 0)}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../pictures/icon7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.continueBtn.setIcon(icon1)
        self.continueBtn.setIconSize(QtCore.QSize(40, 40))
        self.continueBtn.setObjectName("continueBtn")
        self.termLabel = QtWidgets.QTextEdit(Form)
        self.termLabel.setGeometry(QtCore.QRect(30, 200, 300, 160))
        self.termLabel.setStyleSheet("background-color: #F8FAE5;\n"
                                     "font: 13pt \"MS Sans Serif\";\n"
                                     "color: #B19470;\n"
                                     "font-weight: 600;\n"
                                     "border-radius: 8px;\n"
                                     "border: 2px solid #B19470;\n"
                                     "margin-top: 0px;\n"
                                     "outline: 0px;\n"
                                     "hover: { background-color: red };\n"
                                     "pressed: { background-color: rgb(0, 255, 0)}")
        self.termLabel.setReadOnly(True)
        self.termLabel.setObjectName("termLabel")
        self.definitionLabel = QtWidgets.QTextEdit(Form)
        self.definitionLabel.setGeometry(QtCore.QRect(380, 200, 300, 160))
        self.definitionLabel.setStyleSheet("background-color: #F8FAE5;\n"
                                           "font: 13pt \"MS Sans Serif\";\n"
                                           "color: #B19470;\n"
                                           "font-weight: 600;\n"
                                           "border-radius: 8px;\n"
                                           "border: 2px solid #B19470;\n"
                                           "margin-top: 0px;\n"
                                           "outline: 0px;\n"
                                           "hover: { background-color: red };\n"
                                           "pressed: { background-color: rgb(0, 255, 0)}")
        self.definitionLabel.setReadOnly(True)
        self.definitionLabel.setObjectName("definitionLabel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 150, 301, 41))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 18pt \"MS Sans Serif\";\n"
                                 "color: #EEEEEE;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 150, 301, 41))
        self.label_2.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 18pt \"MS Sans Serif\";\n"
                                   "color: #EEEEEE;\n"
                                   "font-weight: 600;\n"
                                   "padding: 5px 15px;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(70, 20, 621, 131))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.continueBtn.setText(_translate("Form", "Продолжить"))
        self.termLabel.setHtml(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.definitionLabel.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "Термин"))
        self.label_2.setText(_translate("Form", "Определение"))

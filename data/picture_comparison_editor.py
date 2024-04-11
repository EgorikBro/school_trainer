from PyQt5 import QtCore, QtGui, QtWidgets


class PictureComparisonEditorUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 528)
        Form.setMinimumSize(QtCore.QSize(831, 528))
        Form.setMaximumSize(QtCore.QSize(831, 528))
        Form.setStyleSheet("background-color: #43766C")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(90, 200, 296, 159))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 150, 281, 41))
        self.label_2.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                   "font: 13pt \"MS Sans Serif\";\n"
                                   "color: #F8FAE5;\n"
                                   "font-weight: 600;\n"
                                   "padding: 5px 15px;\n"
                                   "margin-top: 0px;\n"
                                   "outline: 0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 150, 281, 41))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 13pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 440, 291, 41))
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
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(80, 30, 721, 91))
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
        self.pushButton.setGeometry(QtCore.QRect(50, 440, 361, 41))
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
        self.pictureLabel = QtWidgets.QLabel(Form)
        self.pictureLabel.setGeometry(QtCore.QRect(440, 200, 301, 159))
        self.pictureLabel.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 13pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;\n"
                                        "hover: { background-color: red };\n"
                                        "pressed: { background-color: rgb(0, 255, 0)}")
        self.pictureLabel.setText("")
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setObjectName("pictureLabel")
        self.addPictureBtn = QtWidgets.QPushButton(Form)
        self.addPictureBtn.setGeometry(QtCore.QRect(440, 200, 301, 159))
        self.addPictureBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.addPictureBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                         "font: 10pt \"MS Sans Serif\";\n"
                                         "color: #F8FAE5;\n"
                                         "font-weight: 600;\n"
                                         "margin-top: 0px;\n"
                                         "outline: 0px;")
        self.addPictureBtn.setText("")
        self.addPictureBtn.setFlat(True)
        self.addPictureBtn.setObjectName("addPictureBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_1.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "Картинка"))
        self.label.setText(_translate("Form", "Описание"))
        self.pushButton_2.setText(_translate("Form", "Добавить картинку"))
        self.pushButton.setText(_translate("Form", "Завершить создание теста"))

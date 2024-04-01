from PyQt5 import QtCore, QtGui, QtWidgets


class MainMenuUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #43766C")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 341, 91))
        self.label.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                 "font: 20pt \"MS Sans Serif\";\n"
                                 "color: #F8FAE5;\n"
                                 "font-weight: 600;\n"
                                 "padding: 5px 15px;\n"
                                 "margin-top: 0px;\n"
                                 "outline: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 181, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui\\../pictures/icon1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 90, 141, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../pictures/icon2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 320, 151, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("ui\\../pictures/icon4.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 330, 141, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui\\../pictures/icon5.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 270, 162, 223))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.physicsBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.physicsBtn.setMinimumSize(QtCore.QSize(160, 50))
        self.physicsBtn.setStyleSheet("background-color: #F8FAE5;\n"
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
        self.physicsBtn.setObjectName("physicsBtn")
        self.verticalLayout.addWidget(self.physicsBtn)
        self.biologyBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.biologyBtn.setMinimumSize(QtCore.QSize(160, 50))
        self.biologyBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                      "font: 10pt \"MS Sans Serif\";\n"
                                      "color: #B19470;\n"
                                      "font-weight: 600;\n"
                                      "border-radius: 8px;\n"
                                      "border: 2px solid #B19470;\n"
                                      "padding: 5px 15px;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.biologyBtn.setObjectName("biologyBtn")
        self.verticalLayout.addWidget(self.biologyBtn)
        self.chemistryBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.chemistryBtn.setMinimumSize(QtCore.QSize(160, 50))
        self.chemistryBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 10pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
                                        "padding: 5px 15px;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;")
        self.chemistryBtn.setObjectName("chemistryBtn")
        self.verticalLayout.addWidget(self.chemistryBtn)
        self.geographyBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.geographyBtn.setMinimumSize(QtCore.QSize(160, 50))
        self.geographyBtn.setStyleSheet("background-color: #F8FAE5;\n"
                                        "font: 10pt \"MS Sans Serif\";\n"
                                        "color: #B19470;\n"
                                        "font-weight: 600;\n"
                                        "border-radius: 8px;\n"
                                        "border: 2px solid #B19470;\n"
                                        "padding: 5px 15px;\n"
                                        "margin-top: 0px;\n"
                                        "outline: 0px;")
        self.geographyBtn.setObjectName("geographyBtn")
        self.verticalLayout.addWidget(self.geographyBtn)
        self.avatarLabel = QtWidgets.QLabel(self.centralwidget)
        self.avatarLabel.setGeometry(QtCore.QRect(20, 520, 61, 61))
        self.avatarLabel.setText("")
        self.avatarLabel.setPixmap(QtGui.QPixmap("ui\\../avatars/default_icon.png"))
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setObjectName("avatarLabel")
        self.accountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.accountBtn.setGeometry(QtCore.QRect(90, 540, 16, 28))
        self.accountBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.accountBtn.setStyleSheet("background-color: rgb 0, 0, 0;\n"
                                      "font: 10pt \"MS Sans Serif\";\n"
                                      "color: #F8FAE5;\n"
                                      "font-weight: 600;\n"
                                      "margin-top: 0px;\n"
                                      "outline: 0px;")
        self.accountBtn.setText("")
        self.accountBtn.setFlat(True)
        self.accountBtn.setObjectName("accountBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Тренажёр"))
        self.physicsBtn.setText(_translate("MainWindow", "Физика"))
        self.biologyBtn.setText(_translate("MainWindow", "Биология"))
        self.chemistryBtn.setText(_translate("MainWindow", "Химия"))
        self.geographyBtn.setText(_translate("MainWindow", "География"))

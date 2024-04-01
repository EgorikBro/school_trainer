from PyQt5 import QtCore, QtGui, QtWidgets


class AnswersUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 560)
        Form.setMinimumSize(QtCore.QSize(662, 560))
        Form.setMaximumSize(QtCore.QSize(662, 560))
        Form.setStyleSheet("background-color: #43766C")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 10, 641, 541))
        self.listView.setStyleSheet("background-color: #F8FAE5;\n"
                                    "font: 13pt \"MS Sans Serif\";\n"
                                    "color: #B19470;\n"
                                    "font-weight: 600;\n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid #B19470;\n"
                                    "margin-top: 0px;\n"
                                    "outline: 0px;")
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

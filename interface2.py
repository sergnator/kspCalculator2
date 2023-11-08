from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Error(object):
    def setupUi(self, Ui_MainWindow_Error):
        Ui_MainWindow_Error.setObjectName("MainWindow")
        Ui_MainWindow_Error.resize(445, 309)
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow_Error)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 250, 288, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Yes = QtWidgets.QPushButton(self.widget)
        self.Yes.setDefault(True)
        self.Yes.setObjectName("Yes")
        self.horizontalLayout.addWidget(self.Yes)
        self.No = QtWidgets.QPushButton(self.widget)
        self.No.setAutoDefault(False)
        self.No.setObjectName("No")
        self.horizontalLayout.addWidget(self.No)

        self.retranslateUi(Ui_MainWindow_Error)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow_Error)

    def retranslateUi(self, Ui_MainWindow_Error):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow_Error.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "Произошла ошибка. Дальнейшая работа программы может быть некорректна. Закрыть программу? "))
        self.Yes.setText(_translate("MainWindow", "Да"))
        self.No.setText(_translate("MainWindow", "нет"))

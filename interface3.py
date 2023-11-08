# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, PlanetAdd):
        PlanetAdd.setObjectName("PlanetAdd")
        PlanetAdd.resize(977, 736)
        self.Icon = QtWidgets.QLabel(PlanetAdd)
        self.Icon.setGeometry(QtCore.QRect(20, 560, 361, 151))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("../../../.designer/backup/Images/KspIcon.png"))
        self.Icon.setObjectName("Icon")
        self.layoutWidget = QtWidgets.QWidget(PlanetAdd)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 190, 520, 406))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.acceleration = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acceleration.setFont(font)
        self.acceleration.setObjectName("acceleration")
        self.verticalLayout_2.addWidget(self.acceleration)
        self.atmoph = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.atmoph.setFont(font)
        self.atmoph.setObjectName("atmoph")
        self.verticalLayout_2.addWidget(self.atmoph)
        self.second_space_speed = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.second_space_speed.setFont(font)
        self.second_space_speed.setObjectName("second_space_speed")
        self.verticalLayout_2.addWidget(self.second_space_speed)
        self.color_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.color_button.setFont(font)
        self.color_button.setObjectName("color_button")
        self.verticalLayout_2.addWidget(self.color_button)
        self.alt = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alt.setFont(font)
        self.alt.setObjectName("alt")
        self.verticalLayout_2.addWidget(self.alt)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveBut = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.saveBut.setFont(font)
        self.saveBut.setObjectName("saveBut")
        self.horizontalLayout_2.addWidget(self.saveBut)
        self.cancel = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PlanetAdd)
        QtCore.QMetaObject.connectSlotsByName(PlanetAdd)

    def retranslateUi(self, PlanetAdd):
        _translate = QtCore.QCoreApplication.translate
        PlanetAdd.setWindowTitle(_translate("PlanetAdd", "Добавить планету"))
        self.label.setText(_translate("PlanetAdd", "Имя"))
        self.label_2.setText(_translate("PlanetAdd", "Ускорение"))
        self.label_3.setText(_translate("PlanetAdd", "Атмосфера"))
        self.label_4.setText(_translate("PlanetAdd", "Вторая космическая"))
        self.label_5.setText(_translate("PlanetAdd", "Цвет"))
        self.label_6.setText(_translate("PlanetAdd", "Высота"))
        self.atmoph.setText(_translate("PlanetAdd", "есть"))
        self.color_button.setText(_translate("PlanetAdd", "Выбрать"))
        self.saveBut.setText(_translate("PlanetAdd", "Подтвердить"))
        self.cancel.setText(_translate("PlanetAdd", "Отмена"))
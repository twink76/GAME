# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shop_MiddleMode.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Shop_MiddleMode(object):
    def setupUi(self, Shop_MiddleMode):
        Shop_MiddleMode.setObjectName("Shop_MiddleMode")
        Shop_MiddleMode.resize(880, 380)
        Shop_MiddleMode.setStyleSheet("background-color: #edeef0")
        self.centralwidget = QtWidgets.QWidget(Shop_MiddleMode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(365, 10, 151, 51))
        self.label.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 30px;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 261, 101))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"font-size: 25px;\n"
"color: white;\n"
"background-color: #969393;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #878484;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"font-size: 23px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 90, 261, 101))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"font-size: 25px;\n"
"color: white;\n"
"background-color: #969393;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #878484;\n"
"}\n"
"QPushButton:pressed{\n"
"font-size: 23px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 170, 261, 101))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"font-size: 25px;\n"
"color: white;\n"
"background-color: #969393;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #878484;\n"
"}\n"
"QPushButton:pressed{\n"
"font-size: 23px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_money = QtWidgets.QLabel(self.centralwidget)
        self.label_money.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.label_money.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_money.setObjectName("label_money")
        self.label_hp = QtWidgets.QLabel(self.centralwidget)
        self.label_hp.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.label_hp.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_hp.setObjectName("label_hp")
        self.label_dmg = QtWidgets.QLabel(self.centralwidget)
        self.label_dmg.setGeometry(QtCore.QRect(10, 110, 141, 41))
        self.label_dmg.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_dmg.setObjectName("label_dmg")
        self.label_pay_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_pay_1.setGeometry(QtCore.QRect(10, 290, 261, 41))
        self.label_pay_1.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_pay_1.setObjectName("label_pay_1")
        self.label_pay_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pay_2.setGeometry(QtCore.QRect(610, 290, 261, 41))
        self.label_pay_2.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_pay_2.setObjectName("label_pay_2")
        Shop_MiddleMode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Shop_MiddleMode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName("menubar")
        Shop_MiddleMode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Shop_MiddleMode)
        self.statusbar.setObjectName("statusbar")
        Shop_MiddleMode.setStatusBar(self.statusbar)

        self.retranslateUi(Shop_MiddleMode)
        QtCore.QMetaObject.connectSlotsByName(Shop_MiddleMode)

    def retranslateUi(self, Shop_MiddleMode):
        _translate = QtCore.QCoreApplication.translate
        Shop_MiddleMode.setWindowTitle(_translate("Shop_MiddleMode", "Shop_EasyMode"))
        self.label.setText(_translate("Shop_MiddleMode", "Магазин"))
        self.pushButton.setText(_translate("Shop_MiddleMode", "Увеличить здоровье"))
        self.pushButton_2.setText(_translate("Shop_MiddleMode", "К Битве"))
        self.pushButton_3.setText(_translate("Shop_MiddleMode", "Увеличить урон"))
        self.label_money.setText(_translate("Shop_MiddleMode", "MONEY - "))
        self.label_hp.setText(_translate("Shop_MiddleMode", "HP -"))
        self.label_dmg.setText(_translate("Shop_MiddleMode", "DMG -"))
        self.label_pay_1.setText(_translate("Shop_MiddleMode", "TextLabel"))
        self.label_pay_2.setText(_translate("Shop_MiddleMode", "TextLabel"))

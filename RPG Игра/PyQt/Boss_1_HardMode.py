# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Boss_1_HardMode.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Boss_1_MiddleMode(object):
    def setupUi(self, Boss_1_HardMode):
        Boss_1_HardMode.setObjectName("Boss_1_HardMode")
        Boss_1_HardMode.setGeometry(QtCore.QRect(0, 0, 1240, 720))
        Boss_1_HardMode.setStyleSheet("QMainWindow{\n"
"background: url(images/team.jpg) no-repeat;\n"
"background-color: #edeef0\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Boss_1_HardMode)
        self.centralwidget.setObjectName("centralwidget")
        self.label_boss_hp = QtWidgets.QLabel(self.centralwidget)
        self.label_boss_hp.setGeometry(QtCore.QRect(1060, 600, 161, 41))
        self.label_boss_hp.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_boss_hp.setObjectName("label_boss_hp")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 580, 410, 91))
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
"QPushButton:pressed{\n"
"font-size: 23px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_boss_dmg = QtWidgets.QLabel(self.centralwidget)
        self.label_boss_dmg.setGeometry(QtCore.QRect(515, 20, 210, 41))
        self.label_boss_dmg.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_boss_dmg.setObjectName("label_boss_dmg")
        self.label_money = QtWidgets.QLabel(self.centralwidget)
        self.label_money.setGeometry(QtCore.QRect(10, 630, 181, 41))
        self.label_money.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_money.setObjectName("label_money")
        self.label_hp = QtWidgets.QLabel(self.centralwidget)
        self.label_hp.setGeometry(QtCore.QRect(10, 580, 141, 41))
        self.label_hp.setStyleSheet("QLabel{\n"
"font-family: Areal;\n"
"padding: 5px;\n"
"border: 5px solid #969393;\n"
"border-radius: 15px;\n"
"font-size: 20px;\n"
"}")
        self.label_hp.setObjectName("label_hp")
        Boss_1_HardMode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Boss_1_HardMode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
        self.menubar.setObjectName("menubar")
        Boss_1_HardMode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Boss_1_HardMode)
        self.statusbar.setObjectName("statusbar")
        Boss_1_HardMode.setStatusBar(self.statusbar)

        self.retranslateUi(Boss_1_HardMode)
        QtCore.QMetaObject.connectSlotsByName(Boss_1_HardMode)

    def retranslateUi(self, Boss_1_HardMode):
        _translate = QtCore.QCoreApplication.translate
        Boss_1_HardMode.setWindowTitle(_translate("Boss_1_MiddleMode", "MainWindow"))
        self.label_boss_hp.setText(_translate("Boss_1_MiddleMode", "BOSS HP - "))
        self.pushButton.setText(_translate("Boss_1_MiddleMode", "Ударить"))
        self.label_boss_dmg.setText(_translate("Boss_1_MiddleMode", "Вы напали на босса"))
        self.label_money.setText(_translate("Boss_1_MiddleMode", "MONEY - "))
        self.label_hp.setText(_translate("Boss_1_MiddleMode", "HP -"))

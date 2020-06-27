import sys
sys.path.insert(0, "C:/Python/RPG Игра/PyQt")

from start import *

from Boss_1_EasyMode import *
#from Boss_2_EasyMode import *

from Boss_1_MiddleMode import *
#from Boss_2_MiddleMode import *

from Boss_1_HardMode import *

from Shop_EasyMode import *
from Shop_MiddleMode import *
from Shop_HardMode import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QSlider, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt

from random  import randint


class Start(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Start()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		global EasyMode_boss_1
		global EasyMode_money
		global EasyMode_hp
		global EasyMode_user_dmg

		global MiddleMode_boss_1
		global MiddleMode_money
		global MiddleMode_hp
		global MiddleMode_user_dmg

		global HardMode_boss_1
		global HardMode_money
		global HardMode_hp
		global HardMode_user_dmg

		EasyMode_boss_1 = 5
		EasyMode_money = 0
		EasyMode_hp = 15
		EasyMode_user_dmg = 1

		MiddleMode_boss_1 = 10
		MiddleMode_money = 0
		MiddleMode_hp = 10
		MiddleMode_user_dmg = 1

		HardMode_boss_1 = 10
		HardMode_money = 0
		HardMode_hp = 7
		HardMode_user_dmg = 1

		self.ui.pushButton.clicked.connect(self.Open_EasyMode)
		self.ui.pushButton_2.clicked.connect(self.Open_MidleMode)
		self.ui.pushButton_3.clicked.connect(self.Open_HardMode)

	def Open_EasyMode(self):
		self.close()
		self.Boss_1_EasyMode = Boss_1_EasyMode()
		self.Boss_1_EasyMode.show()

	def Open_MidleMode(self):
		self.close()
		self.Boss_1_MiddleMode = Boss_1_MiddleMode()
		self.Boss_1_MiddleMode.show()

	def Open_HardMode(self):

		self.close()
		self.Boss_1_HardMode = Boss_1_HardMode()
		self.Boss_1_HardMode.show()



###################################################################################################################################################################################################################################################



class Boss_1_EasyMode(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Boss_1_EasyMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.ui.label_hp.setText('HP - ' + str(EasyMode_hp))
		self.ui.label_money.setText('MONEY - ' + str(EasyMode_money))
		self.ui.label_boss_hp.setText('BOSS HP - ' + str(EasyMode_boss_1))

		self.hp = EasyMode_hp
		self.boss_1 = EasyMode_boss_1
		self.user_dmg = EasyMode_user_dmg
		self.money = EasyMode_money

		self.ui.pushButton.clicked.connect(self.NewBoss_1_EasyMode)


	def NewBoss_1_EasyMode(self):

		if self.boss_1 > 0:
			self.miss_chance = randint(1, 4) # Шанс на промах вашего удараz
			self.dmg1 = randint(1, 3) # Урон от босса

			if self.miss_chance == 1:
				self.hp -= self.dmg1
				self.ui.label_boss_dmg.setText('Вы не попали по боссу\nУрон босса по вам: ' + str(self.dmg1) )						
				self.ui.label_boss_dmg.adjustSize()
				self.ui.label_hp.setText('HP - ' + str(self.hp))
				if self.hp < 1:
					self.ui.label_hp.setText('HP - ' + str(0))
					QMessageBox.information(None, 'Вы погибли', "Начать с начала")
					self.close()
					self.Start = Start()
					self.Start.show()
				else:
					pass
			else:
				
				self.ui.label_boss_dmg.setText('Вы ударили босса\nВаш урон по боссу: ' + str(self.user_dmg))
				self.ui.label_boss_dmg.adjustSize()
				self.boss_1 = int(self.boss_1)
				self.boss_1 = self.boss_1 - self.user_dmg
				self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

				if self.boss_1 <= 0:

					self.ui.label_boss_hp.setText('BOSS HP - ' + str(0))
					self.win_money = 100
					self.money += self.win_money


					global EasyMode_money
					global EasyMode_hp
					global EasyMode_user_dmg
					#global EasyMode_boss_1
					EasyMode_money = self.money
					EasyMode_hp = self.hp
					EasyMode_user_dmg = self.user_dmg

					self.ui.label_boss_dmg.setText('Вы победили босса!!!')
					self.ui.pushButton.setText('Перейти в магазин')
					QMessageBox.information(None, 'Поздравляем', "Вы получили " + str(self.win_money) + " монет")
					self.ui.pushButton.clicked.connect(self.Open_Shop_EasyMode)
	

	def Open_Shop_EasyMode(self):
		self.close()
		self.Shop_EasyMode = Shop_EasyMode()
		self.Shop_EasyMode.show()


"""
class Boss_2_EasyMode(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Boss_2_EasyMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.hp = EasyMode_hp
		self.user_dmg = EasyMode_user_dmg
		self.money = EasyMode_money
		self.boss_1 = EasyMode_boss_1

		self.ui.label_hp.setText('HP - ' + str(self.hp))
		self.ui.label_money.setText('MONEY - ' + str(self.money))
		self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

		self.ui.pushButton.clicked.connect(self.NewBoss_2_EasyMode)

	def NewBoss_2_EasyMode(self):

		if self.boss_1 > 0:
			self.miss_chance = randint(1, 4) # Шанс на промах вашего удараz
			self.dmg1 = randint(1, 3) # Урон от босса

			if self.miss_chance == 1:
				self.hp -= self.dmg1
				self.ui.label_boss_dmg.setText('Вы не попали по боссу\nУрон босса по вам: ' + str(self.dmg1) )						
				self.ui.label_boss_dmg.adjustSize()
				self.ui.label_hp.setText('HP - ' + str(self.hp))
				if self.hp < 1:
					self.ui.label_hp.setText('HP - ' + str(0))
					self.ui.label_boss_dmg.setText('Вы погибли :(')
					self.ui.label_boss_dmg.adjustSize()
					self.ui.pushButton.setText('Что бы начать с начала - нажмите')

					self.ui.pushButton.clicked.connect(self.Restart_EasyMode)
				else:
					pass
			else:
				
				self.ui.label_boss_dmg.setText('Вы ударили босса\nВаш урон по боссу: ' + str(self.user_dmg))
				self.ui.label_boss_dmg.adjustSize()
				self.boss_1 = int(self.boss_1)
				self.boss_1 = self.boss_1 - self.user_dmg

				if self.boss_1 >= 0:
					self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))
				else:
					self.ui.label_boss_hp.setText('BOSS HP - ' + str(0))

				if self.boss_1 <= 0:

					self.win_money = 100
					self.money += self.win_money

					global EasyMode_money
					global EasyMode_hp
					global EasyMode_user_dmg
					#global EasyMode_boss_1
					EasyMode_money = self.money
					EasyMode_hp = self.hp
					EasyMode_user_dmg = self.user_dmg
					#EasyMode_boss_1 = self.boss_1 + 5

					self.ui.label_boss_dmg.setText('Вы победили босса!!!')
					self.ui.pushButton.setText('Перейти в магазин')
					QMessageBox.information(None, 'Поздравляем', "Вы получили " + str(self.win_money) + " монет")
					self.ui.pushButton.clicked.connect(self.Open_Shop_EasyMode)
	
	
	def Restart_EasyMode(self):
		self.close()
		self.Start = Start()
		self.Start.show()

	def Open_Shop_EasyMode(self):
		self.close()
		self.Shop_EasyMode = Shop_EasyMode()
		self.Shop_EasyMode.show()


"""

class Shop_EasyMode(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Shop_EasyMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.ui.label_hp.setText('HP - ' + str(EasyMode_hp))
		self.ui.label_money.setText('MONEY - ' + str(EasyMode_money))
		self.ui.label_dmg.setText('DMG - ' + str(EasyMode_user_dmg))
		self.ui.label_pay_1.setText('Цена 50; HP + 2')
		self.ui.label_pay_2.setText('Цена 100; DMG + 1')

		self.EasyMode_hp = EasyMode_hp
		self.EasyMode_money = EasyMode_money
		self.EasyMode_user_dmg = EasyMode_user_dmg

		self.ui.pushButton.clicked.connect(self.Hp_Up_EasyMode)
		self.ui.pushButton_2.clicked.connect(self.Open_NewBoss_1_EasyMode)
		self.ui.pushButton_3.clicked.connect(self.Dmg_Up_EasyMode)

	def Hp_Up_EasyMode(self):

		if self.EasyMode_money - 50 >= 0:

			self.EasyMode_hp += 2
			self.EasyMode_money -= 50

			self.ui.label_hp.setText('HP - ' + str(self.EasyMode_hp))
			self.ui.label_money.setText('MONEY - ' + str(self.EasyMode_money))
			
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Dmg_Up_EasyMode(self):

		if self.EasyMode_money - 100 >= 0:
			
			self.EasyMode_user_dmg += 1
			self.EasyMode_money -= 100

			self.ui.label_dmg.setText('DMG - ' + str(self.EasyMode_user_dmg))
			self.ui.label_money.setText('MONEY - ' + str(self.EasyMode_money))
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Open_NewBoss_1_EasyMode(self):

		global EasyMode_money
		global EasyMode_hp
		global EasyMode_user_dmg
		global EasyMode_boss_1
		EasyMode_money = self.EasyMode_money
		EasyMode_hp = self.EasyMode_hp
		EasyMode_user_dmg = self.EasyMode_user_dmg
		EasyMode_boss_1 += 5

		self.close()
		self.Boss_1_EasyMode = Boss_1_EasyMode()
		self.Boss_1_EasyMode.show()



###################################################################################################################################################################################################################################################



class Boss_1_MiddleMode(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Boss_1_MiddleMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.hp = MiddleMode_hp
		self.boss_1 = MiddleMode_boss_1
		self.user_dmg = MiddleMode_user_dmg
		self.money = MiddleMode_money

		self.ui.label_hp.setText('HP - ' + str(self.hp))
		self.ui.label_money.setText('MONEY - ' + str(self.money))
		self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

		self.ui.pushButton.clicked.connect(self.NewBoss_1_MiddleMode)


	def NewBoss_1_MiddleMode(self):

		if self.boss_1 > 0:
			self.miss_chance = randint(1, 4) # Шанс на промах вашего удараz
			self.dmg1 = randint(1, 3) # Урон от босса

			if self.miss_chance == 1:
				self.hp -= self.dmg1

				if self.hp < 1:
					self.ui.label_hp.setText('HP - ' + str(0))

					QMessageBox.information(None, 'Вы погибли', "Начать с начала")
					self.close()
					self.Start = Start()
					self.Start.show()

				else:
					self.ui.label_hp.setText('HP - ' + str(self.hp))
					self.ui.label_boss_dmg.setText('Вы не попали по боссу\nУрон босса по вам: ' + str(self.dmg1) )						
					self.ui.label_boss_dmg.adjustSize()
			
			else:
				
				self.ui.label_boss_dmg.setText('Вы ударили босса\nВаш урон по боссу: ' + str(self.user_dmg))
				self.ui.label_boss_dmg.adjustSize()
				self.boss_1 = int(self.boss_1)
				self.boss_1 = self.boss_1 - self.user_dmg
				self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

				if self.boss_1 <= 0:

					self.ui.label_boss_hp.setText('BOSS HP - ' + str(0))
					self.win_money = 100
					self.money += self.win_money


					global MiddleMode_money
					global MiddleMode_hp
					global MiddleMode_user_dmg
					#global EasyMode_boss_1
					MiddleMode_money = self.money
					MiddleMode_hp = self.hp
					MiddleMode_user_dmg = self.user_dmg

					self.ui.label_boss_dmg.setText('Вы победили босса!!!')
					self.ui.pushButton.setText('Перейти в магазин')
					QMessageBox.information(None, 'Поздравляем', "Вы получили " + str(self.win_money) + " монет")
					self.ui.pushButton.clicked.connect(self.Open_Shop_MiddleMode)

	def Open_Shop_MiddleMode(self):
		self.close()
		self.Shop_MiddleMode = Shop_MiddleMode()
		self.Shop_MiddleMode.show()

"""

class Boss_2_MiddleMode(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Boss_2_MiddleMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.hp = MiddleMode_hp
		self.user_dmg = MiddleMode_user_dmg
		self.money = MiddleMode_money
		self.boss_1 = MiddleMode_boss_1

		self.ui.label_hp.setText('HP - ' + str(self.hp))
		self.ui.label_money.setText('MONEY - ' + str(self.money))
		self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

		self.ui.pushButton.clicked.connect(self.NewBoss_2_MiddleMode)

	def NewBoss_2_MiddleMode(self):

		if self.boss_1 > 0:
			self.miss_chance = randint(1, 4) # Шанс на промах вашего удараz
			self.dmg1 = randint(1, 3) # Урон от босса

			if self.miss_chance == 1:
				self.hp -= self.dmg1
				self.ui.label_boss_dmg.setText('Вы не попали по боссу\nУрон босса по вам: ' + str(self.dmg1) )						
				self.ui.label_boss_dmg.adjustSize()
				self.ui.label_hp.setText('HP - ' + str(self.hp))
				if self.hp < 1:
					self.ui.label_hp.setText('HP - ' + str(0))
					self.ui.label_boss_dmg.setText('Вы погибли :(')
					self.ui.label_boss_dmg.adjustSize()
					self.ui.pushButton.setText('Что бы начать с начала - нажмите')

					self.ui.pushButton.clicked.connect(self.Restart_EasyMode)
				else:
					pass
			else:
				
				self.ui.label_boss_dmg.setText('Вы ударили босса\nВаш урон по боссу: ' + str(self.user_dmg))
				self.ui.label_boss_dmg.adjustSize()
				self.boss_1 = int(self.boss_1)
				self.boss_1 = self.boss_1 - self.user_dmg

				if self.boss_1 >= 0:
					self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))
				else:
					self.ui.label_boss_hp.setText('BOSS HP - ' + str(0))

				if self.boss_1 <= 0:

					self.win_money = 100
					self.money += self.win_money

					global MiddleMode_money
					global MiddleMode_hp
					global MiddleMode_user_dmg
					#global EasyMode_boss_1
					MiddleMode_money = self.money
					MiddleMode_hp = self.hp
					MiddleMode_user_dmg = self.user_dmg
					#EasyMode_boss_1 = self.boss_1 + 5

					self.ui.label_boss_dmg.setText('Вы победили босса!!!')
					self.ui.pushButton.setText('Перейти в магазин')
					QMessageBox.information(None, 'Поздравляем', "Вы получили " + str(self.win_money) + " монет")
					self.ui.pushButton.clicked.connect(self.Open_Shop_MiddleMode)
	
	
	def Restart_MiddleMode(self):
		self.close()
		self.Start = Start()
		self.Start.show()

	def Open_Shop_MiddleMode(self):
		self.close()
		self.Shop_MiddleMode = Shop_MiddleMode()
		self.Shop_MiddleMode.show()

"""


class Shop_MiddleMode(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Shop_MiddleMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.ui.label_hp.setText('HP - ' + str(MiddleMode_hp))
		self.ui.label_money.setText('MONEY - ' + str(MiddleMode_money))
		self.ui.label_dmg.setText('DMG - ' + str(MiddleMode_user_dmg))
		self.ui.label_pay_1.setText('Цена 50; HP + 2')
		self.ui.label_pay_2.setText('Цена 150; DMG + 1')

		self.MiddleMode_hp = MiddleMode_hp
		self.MiddleMode_money = MiddleMode_money
		self.MiddleMode_user_dmg = MiddleMode_user_dmg

		self.ui.pushButton.clicked.connect(self.Hp_Up_MiddleMode)
		self.ui.pushButton_2.clicked.connect(self.Open_NewBoss_1_MiddleMode)
		self.ui.pushButton_3.clicked.connect(self.Dmg_Up_MiddleMode)

	def Hp_Up_MiddleMode(self):

		if self.MiddleMode_money - 50 >= 0:

			self.MiddleMode_hp += 2
			self.MiddleMode_money -= 50

			self.ui.label_hp.setText('HP - ' + str(self.MiddleMode_hp))
			self.ui.label_money.setText('MONEY - ' + str(self.MiddleMode_money))
			
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Dmg_Up_MiddleMode(self):

		if self.MiddleMode_money - 150 >= 0:
			
			self.MiddleMode_user_dmg += 1
			self.MiddleMode_money -= 150

			self.ui.label_dmg.setText('DMG - ' + str(self.MiddleMode_user_dmg))
			self.ui.label_money.setText('MONEY - ' + str(self.MiddleMode_money))
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Open_NewBoss_1_MiddleMode(self):

		global MiddleMode_money
		global MiddleMode_hp
		global MiddleMode_user_dmg
		global MiddleMode_boss_1
		MiddleMode_money = self.MiddleMode_money
		MiddleMode_hp = self.MiddleMode_hp
		MiddleMode_user_dmg = self.MiddleMode_user_dmg
		MiddleMode_boss_1 += 5

		self.close()
		self.Boss_1_MiddleMode = Boss_1_MiddleMode()
		self.Boss_1_MiddleMode.show()



###################################################################################################################################################################################################################################################




class Boss_1_HardMode(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Boss_1_HardMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.hp = HardMode_hp
		self.boss_1 = HardMode_boss_1
		self.user_dmg = HardMode_user_dmg
		self.money = HardMode_money

		self.ui.label_hp.setText('HP - ' + str(self.hp))
		self.ui.label_money.setText('MONEY - ' + str(self.money))
		self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

		self.ui.pushButton.clicked.connect(self.NewBoss_1_HardMode)


	def NewBoss_1_HardMode(self):

		if self.boss_1 > 0:
			self.miss_chance = randint(1, 4) # Шанс на промах вашего удараz
			self.dmg1 = randint(1, 3) # Урон от босса

			if self.miss_chance == 1:
				self.hp -= self.dmg1
				self.ui.label_boss_dmg.setText('Вы не попали по боссу\nУрон босса по вам: ' + str(self.dmg1) )						
				self.ui.label_boss_dmg.adjustSize()
				self.ui.label_hp.setText('HP - ' + str(self.hp))
				if self.hp < 1:
					self.ui.label_hp.setText('HP - ' + str(0))
					QMessageBox.information(None, 'Вы погибли', "Начать с начала")
					self.close()
					self.Start = Start()
					self.Start.show()
				else:
					pass
			else:
				
				self.ui.label_boss_dmg.setText('Вы ударили босса\nВаш урон по боссу: ' + str(self.user_dmg))
				self.ui.label_boss_dmg.adjustSize()
				self.boss_1 = int(self.boss_1)
				self.boss_1 = self.boss_1 - self.user_dmg
				self.ui.label_boss_hp.setText('BOSS HP - ' + str(self.boss_1))

				if self.boss_1 <= 0:

					self.ui.label_boss_hp.setText('BOSS HP - ' + str(0))
					self.win_money = 75
					self.money += self.win_money


					global HardMode_money
					global HardMode_hp
					global HardMode_user_dmg
					#global EasyMode_boss_1
					HardMode_money = self.money
					HardMode_hp = self.hp
					HardMode_user_dmg = self.user_dmg

					self.ui.label_boss_dmg.setText('Вы победили босса!!!')
					self.ui.pushButton.setText('Перейти в магазин')
					QMessageBox.information(None, 'Поздравляем', "Вы получили " + str(self.win_money) + " монет")
					self.ui.pushButton.clicked.connect(self.Open_Shop_HardMode)


	def Open_Shop_HardMode(self):
		self.close()
		self.Shop_HardMode = Shop_HardMode()
		self.Shop_HardMode.show()


class Shop_HardMode(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Shop_HardMode()
		self.ui.setupUi(self)
		self.setFixedSize(self.size())

		self.ui.label_hp.setText('HP - ' + str(HardMode_hp))
		self.ui.label_money.setText('MONEY - ' + str(HardMode_money))
		self.ui.label_dmg.setText('DMG - ' + str(HardMode_user_dmg))
		self.ui.label_pay_1.setText('Цена 50; HP + 2')
		self.ui.label_pay_2.setText('Цена 150; DMG + 1')

		self.HardMode_hp = HardMode_hp
		self.HardMode_money = HardMode_money
		self.HardMode_user_dmg = HardMode_user_dmg

		self.ui.pushButton.clicked.connect(self.Hp_Up_HardMode)
		self.ui.pushButton_2.clicked.connect(self.Open_NewBoss_1_HardMode)
		self.ui.pushButton_3.clicked.connect(self.Dmg_Up_HardMode)

	def Hp_Up_HardMode(self):

		if self.HardMode_money - 50 >= 0:

			self.HardMode_hp += 2
			self.HardMode_money -= 50

			self.ui.label_hp.setText('HP - ' + str(self.HardMode_hp))
			self.ui.label_money.setText('MONEY - ' + str(self.HardMode_money))
			
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Dmg_Up_HardMode(self):

		if self.HardMode_money - 150 >= 0:
			
			self.HardMode_user_dmg += 1
			self.HardMode_money -= 150

			self.ui.label_dmg.setText('DMG - ' + str(self.HardMode_user_dmg))
			self.ui.label_money.setText('MONEY - ' + str(self.HardMode_money))
		else:
			QMessageBox.information(None, 'Ошибка', "У вас недостаточно монет")

	def Open_NewBoss_1_HardMode(self):

		global HardMode_money
		global HardMode_hp
		global HardMode_user_dmg
		global HardMode_boss_1
		HardMode_money = self.HardMode_money
		HardMode_hp = self.HardMode_hp
		HardMode_user_dmg = self.HardMode_user_dmg
		HardMode_boss_1 += 5

		self.close()
		self.Boss_1_HardMode = Boss_1_HardMode()
		self.Boss_1_HardMode.show()



###################################################################################################################################################################################################################################################



if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Start()

	myapp.show()
	sys.exit(app.exec_())
	
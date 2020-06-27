# удачи ебать)
def Easy():

	money = 0
	a = 1
	hp = 15
	boss_1 = 5
	boss_2 = 0
	man = 3

	from random import randint

	from colorama import init
	from colorama import Fore, Back, Style
	init()

	print(Back.MAGENTA)
	s = input ("Нажмите 'Enter', чтобы играть\n")

	while boss_1 < 21:
		hp1 = hp

		while hp > 0:
			print(Back.MAGENTA)
			print("Контрольная точка")
			print(Back.RED)
			print("Вы напали на босса")
			boss_1 = boss_2 + 5
			boss_2 = boss_1
			while boss_1 > 0 and boss_1 < 20:
				print(Back.RED)       
				print("У босса " + str(boss_1)+ " здоровья")
				s1 = input ("Напишите 'Удар', что бы нанести урон ")
				if s1 == "Удар" or s1 == "удар":
					print ("Вы ударили босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a
				else:
					dmg1 = randint(1, 3)		
					print(Back.CYAN)	
					print ("Вы не попали по боссу, он ударил вас, сняв " + str(dmg1) + " здоровья")
					hp = hp - dmg1
					print ("У вас осталось " + str(hp) + " здоровья")
					if hp < 1:
						print("Вы погибли :( ")
						hp = hp1
						boss_1 = boss_2
						o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
						if o == "Продолжить" or o == "продолжить":
							continue
						else:
							exit(0)

	# Босс 			

			print(Back. GREEN)
			print("У вас " + str(a) + " урона")
			while boss_1 > 0:
				print(Back.RED)
				print("У Босса " + str(boss_1) + " здоровья\nУ Приспешника " + str(man) + " здоровья")
				print(Back.GREEN)
				print("У вас " + str(hp) + " здоровья")
				s1 = input("Кого ударить?\n")
				if s1 == "босса" or s1 == "Босса" or s1 == "босс" or s1 == "Босс":
					print(Back.RED)
					print ("Вы ударили Босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a 
					if boss_1 < 1:
						dmg1 = 0
						dmg2 = 0
						print(Back.RED)
						print("У Босса 0 здоровья")
						print(Back.MAGENTA)
						print("ВЫ ПОБЕДИТЕЛЬ ИГРЫ НАХУЙ ВСЕ!!!")
						print(Back.CYAN)
						b = input("Чтобы выйти нажмите 'Enter'")
						if b == "twink":
							print(Back.MAGENTA)
							print("Ты кто? Нашел пасхалку(молодец)")
							input()
							exit(0)
						else:
								exit(0)						
					if man < 1:
						dmg1 = randint(1, 3)
						dmg2 = 0
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1			
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)	
					else:
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)			
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1			
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)	

	# Приспешник	

				elif s1 == "приспешника" or s1 == "Приспешника" or s1 == "приспешник" or s1 == "Приспешник":
					print(Back.RED)
					print ("Вы ударили Приспешника")
					man = int(man)
					man = man - a
					if man > 0:	
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)	
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)
				
					else:
						dmg1 = randint(1, 3)
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1
						print(Back.MAGENTA)
						print("Приспешник мертв")
						man = 0
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)
						continue

	# Пре-Магазин
			
			money = money + 100
			print(Back.GREEN)
			print("Вы победили босса и получили 100 монет! В вашем кошельке " + str(money) + " монет")
			print(Back.YELLOW) 	
			print("Еще один босс на подходе. Хотите ли вы сразиться с ним или перейти в магазин?")
			print(Back.GREEN)
			next_lvl = input ("Босс\nМагазин\n")
			

			if next_lvl == "Босс" or next_lvl == "босс" or next_lvl == "1":
				continue
			elif next_lvl == "Магазин" or next_lvl == "магазин" or next_lvl == "2":
				print("\nВы в магазине")
				break
			else: 
				print(Back.CYAN)
				print("Ошибка. Преход в магазин")	
				break
	# Магазин

		while money > 0:

			print(Back.YELLOW)
			h = input("Чтобы увеличить урон на 2 ед. за 100 монет - введите '1'\nЧтобы увеличить здоровье на 2 ед. за 50 монет - введите '2'\nЧтобы отказаться от повышения урона или здоровья - введите '0'\n")

			if h == "1":
				money = money - 100
				a = a + 2
				print(Back.GREEN)        		
				print("Урон увеличен на 2 ед.")
				print("Теперь у вас " + str(a) + " урона")
			elif h == "2":
				money = money - 50
				hp = hp + 2
				print(Back.GREEN)        		
				print("Здоровье увеличено на 2 ед.")
				print("У вас " + str(hp) + " здоровья")
			elif h == "0" or h == "нет" or h == "Нет":
				money = money + 0
				a = a + 0
				hp = hp + 0
				print(Back.GREEN)
				print("Урон и Здоровье не повышено")
			else:
				print(Back.MAGENTA)
				print("Вы ошиблись. С вас снято 30 монет")
				money = money - 30
				break

	# Пост-Магазин

			print("У вас " + str(money) + " монет")
			repeat = input("Хотите ли вы улучшить еще что-то?\nДа\nНет\n")
			if repeat == "Да" or repeat == "да":
				if money < 1:
					print(Back.YELLOW)
					print("У вас нет денег, вы перешли к бистве с боссом")
					break
					continue
				else:
					continue
			elif repeat == "Нет" or repeat == "нет":			
				answ = input("\nХотите ли вы сразиться с боссом?\nДа\nНет\n")
				if answ == "Да" or answ == "да":
					break
					continue
				elif answ == "Нет" or answ == "нет":
					print(Back.MAGENTA)
					print("Вы не прошли игру!")
					g = input("Хотите запустить с контрольной точки?\n")
					if g == "Да" or g == "да":
						break
					elif g == "Нет" or g == "нет":
						print(Back.CYAN)
						print("Прощайте :(")
						input()
						exit(0)
					else: 
						exit(0)

		input()

###################################################################################################################################################################################################################################################

def Midle():

	money = 0
	a = 1
	hp = 10
	boss_1 = 5
	boss_2 = 0
	man = 4

	from random import randint

	from colorama import init
	from colorama import Fore, Back, Style
	init()

	print(Back.MAGENTA)
	s = input ("Нажмите 'Enter', чтобы играть\n")

	while boss_1 < 21:
		hp1 = hp

		while hp > 0:
			print(Back.MAGENTA)
			print("Контрольная точка")
			print(Back.RED)
			print("Вы напали на босса")
			boss_1 = boss_2 + 5
			boss_2 = boss_1
			while boss_1 > 0 and boss_1 < 20:
				print(Back.RED)       
				print("У босса " + str(boss_1)+" здоровья")
				s1 = input ("Напишите 'Удар', что бы нанести урон ")
				if s1 == "Удар" or s1 == "удар":
					print ("Вы ударили босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a
				else:
					dmg1 = randint(1, 3)		
					print(Back.CYAN)	
					print ("Вы не попали по боссу, он ударил вас, сняв " + str(dmg1) + " здоровья")
					hp = hp - dmg1
					print ("У вас осталось " + str(hp) + " здоровья")
					if hp < 1:
						print("Вы погибли :( ")
						hp = hp1
						boss_1 = boss_2
						o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
						if o == "Продолжить" or o == "продолжить":
							continue
						else:
							exit(0)

	# Босс 			

			print(Back. GREEN)
			print("У вас " + str(a) + " урона")
			while boss_1 > 0:
				print(Back.RED)
				print("У Босса " + str(boss_1) + " здоровья\nУ Приспешника " + str(man) + " здоровья")
				print(Back.GREEN)
				print("У вас " + str(hp) + " здоровья")
				s1 = input("Кого ударить?\n")
				if s1 == "босса" or s1 == "Босса" or s1 == "босс" or s1 == "Босс":
					print(Back.RED)
					print ("Вы ударили Босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a 
					if boss_1 < 1:
						dmg1 = 0
						dmg2 = 0
						print(Back.RED)
						print("У Босса 0 здоровья")
						print(Back.MAGENTA)
						print("ВЫ ПОБЕДИТЕЛЬ ИГРЫ НАХУЙ ВСЕ!!!")
						print(Back.CYAN)
						b = input("Чтобы выйти нажмите 'Enter'")
						if b == "twink":
							print(Back.MAGENTA)
							print("Ты кто? Нашел пасхалку(молодец)")
							input()
							exit(0)
						else:
								exit(0)						
					if man < 1:
						dmg1 = randint(1, 3)
						dmg2 = 0
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1			
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)	
					else:
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)			
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1			
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)	

	# Приспешник	

				elif s1 == "приспешника" or s1 == "Приспешника" or s1 == "приспешник" or s1 == "Приспешник":
					print(Back.RED)
					print ("Вы ударили Приспешника")
					man = int(man)
					man = man - a
					if man > 0:	
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)	
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)
				
					else:
						dmg1 = randint(1, 3)
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1
						print(Back.MAGENTA)
						print("Приспешник мертв")
						man = 0
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								continue
							else:
								exit(0)
						continue

	# Пре-Магазин
			
			money = money + 100
			print(Back.GREEN)
			print("Вы победили босса и получили 100 монет! В вашем кошельке " + str(money) + " монет")
			print(Back.YELLOW) 	
			print("Еще один босс на подходе. Хотите ли вы сразиться с ним или перейти в магазин?")
			print(Back.GREEN)
			next_lvl = input ("Босс\nМагазин\n")
			

			if next_lvl == "Босс" or next_lvl == "босс" or next_lvl == "1":
				continue
			elif next_lvl == "Магазин" or next_lvl == "магазин" or next_lvl == "2":
				print("\nВы в магазине")
				break
			else: 
				print(Back.CYAN)
				print("Ошибка. Преход в магазин")	
				break
	# Магазин

		while money > 0:

			print(Back.YELLOW)
			h = input("Чтобы увеличить урон на 1 ед. за 100 монет - введите '1'\nЧтобы увеличить здоровье на 2 ед. за 50 монет - введите '2'\nЧтобы отказаться от повышения урона или здоровья - введите '0'\n")

			if h == "1":
				money = money - 100
				a = a + 1
				print(Back.GREEN)        		
				print("Урон увеличен на 1 ед.")
				print("Теперь у вас " + str(a) + " урона")
			elif h == "2":
				money = money - 50
				hp = hp + 2
				print(Back.GREEN)        		
				print("Здоровье увеличено на 2 ед.")
				print("У вас " + str(hp) + " здоровья")
			elif h == "0" or h == "нет" or h == "Нет":
				money = money + 0
				a = a + 0
				hp = hp + 0
				print(Back.GREEN)
				print("Урон и Здоровье не повышено")
			else:
				print(Back.MAGENTA)
				print("Вы ошиблись. С вас снято 30 монет")
				money = money - 30
				break

	# Пост-Магазин

			print("У вас " + str(money) + " монет")
			repeat = input("Хотите ли вы улучшить еще что-то?\nДа\nНет\n")
			if repeat == "Да" or repeat == "да":
				if money < 1:
					print(Back.YELLOW)
					print("У вас нет денег, вы перешли к бистве с боссом")
					break
					continue
				else:
					continue
			elif repeat == "Нет" or repeat == "нет":			
				answ = input("\nХотите ли вы сразиться с боссом?\nДа\nНет\n")
				if answ == "Да" or answ == "да":
					break
					continue
				elif answ == "Нет" or answ == "нет":
					print(Back.MAGENTA)
					print("Вы не прошли игру!")
					g = input("Хотите запустить с контрольной точки?")
					if g == "Да" or g == "да":
						break
					else: 
						print(Back.CYAN)
						print("Ошибка")
						exit(0)

		input()

###################################################################################################################################################################################################################################################

def Hard():

	money = 0
	a = 1
	hp = 8
	boss_1 = 5
	boss_2 = 0
	man = 5

	from random import randint

	from colorama import init
	from colorama import Fore, Back, Style
	init()

	print(Back.MAGENTA)
	s = input ("Нажмите 'Enter', чтобы играть\n")

	while boss_1 < 21:
		hp1 = hp

		while hp > 0:
			print(Back.RED)
			print("Вы напали на босса")
			boss_1 = boss_2 + 5
			boss_2 = boss_1
			while boss_1 > 0 and boss_1 < 20:
				print(Back.RED)       
				print("У босса " + str(boss_1)+" здоровья")
				s1 = input ("Напишите 'Удар', что бы нанести урон ")
				if s1 == "Удар" or s1 == "удар":
					print ("Вы ударили босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a
				else:
					dmg1 = randint(1, 3)		
					print(Back.CYAN)	
					print ("Вы не попали по боссу, он ударил вас, сняв " + str(dmg1) + " здоровья")
					hp = hp - dmg1
					print ("У вас осталось " + str(hp) + " здоровья")
					if hp < 1:
						print("Вы погибли :( ")
						hp = hp1
						boss_1 = boss_2
						o = input("Напишите 'продолжить', чтобы запустить игру с начала, а чтобы закончить нажмите 'Enter'")
						if o == "Продолжить" or o == "продолжить":
							break
							continue
						else:
							exit(0)

	# Босс 			

			print(Back. GREEN)
			print("У вас " + str(a) + " урона")
			while boss_1 > 0:
				print(Back.RED)
				print("У Босса " + str(boss_1) + " здоровья\nУ Приспешника " + str(man) + " здоровья")
				print(Back.GREEN)
				print("У вас " + str(hp) + " здоровья")
				s1 = input("Кого ударить?\n")
				if s1 == "босса" or s1 == "Босса" or s1 == "босс" or s1 == "Босс":
					print(Back.RED)
					print ("Вы ударили Босса")
					boss_1 = int(boss_1)
					boss_1 = boss_1 - a 
					if boss_1 < 1:
						dmg1 = 0
						dmg2 = 0
						print(Back.RED)
						print("У Босса 0 здоровья")
						print(Back.MAGENTA)
						print("ВЫ ПОБЕДИТЕЛЬ ИГРЫ НАХУЙ ВСЕ!!!")
						print(Back.CYAN)
						b = input("Чтобы выйти нажмите 'Enter'")
						if b == "twink":
							print(Back.MAGENTA)
							print("Ты кто? Нашел пасхалку(молодец)")
							input()
							exit(0)
						else:
								exit(0)						
					if man < 1:
						dmg1 = randint(1, 3)
						dmg2 = 0
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1			
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с начала, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								break
								continue
							else:
								exit(0)	
					else:
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)			
						print("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1			
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с начала, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								break
								continue
							else:
								exit(0)	

	# Приспешник	

				elif s1 == "приспешника" or s1 == "Приспешника" or s1 == "приспешник" or s1 == "Приспешник":
					print(Back.RED)
					print ("Вы ударили Приспешника")
					man = int(man)
					man = man - a
					if man > 0:	
						dmg1 = randint(1, 3)
						dmg2 = randint(1, 2)	
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						print ("Приспешник ударил вас, нанеся " + str(dmg2) + " урона")
						hp = hp - dmg1
						hp = hp - dmg2
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								break
								continue
							else:
								exit(0)
				
					else:
						dmg1 = randint(1, 3)
						print ("Босс ударил вас, нанеся " + str(dmg1) + " урона")
						hp = hp - dmg1
						print(Back.MAGENTA)
						print("Приспешник мертв")
						man = 0
						if hp < 1:
							print("Вы погибли :( ")
							hp = hp1
							boss_1 = boss_2
							man = 5
							o = input("Напишите 'продолжить', чтобы запустить игру с контрольной точки, а чтобы закончить нажмите 'Enter'")
							if o == "Продолжить" or o == "продолжить":
								break
								continue
							else:
								exit(0)
						continue

	# Пре-Магазин
			
			money = money + 100
			print(Back.GREEN)
			print("Вы победили босса и получили 100 монет! В вашем кошельке " + str(money) + " монет")
			print(Back.YELLOW) 	
			print("Еще один босс на подходе. Хотите ли вы сразиться с ним или перейти в магазин?")
			print(Back.GREEN)
			next_lvl = input ("Босс\nМагазин\n")
			

			if next_lvl == "Босс" or next_lvl == "босс" or next_lvl == "1":
				continue
			elif next_lvl == "Магазин" or next_lvl == "магазин" or next_lvl == "2":
				print("\nВы в магазине")
				break
			else: 
				print(Back.CYAN)
				print("Ошибка. Преход в магазин")	
				break
	# Магазин

		while money > 0:

			print(Back.YELLOW)
			h = input("Чтобы увеличить здоровье на 2 ед. за 50 монет - введите '2'\nЧтобы отказаться от повышения урона или здоровья - введите '0'\n")

			if h == "2":
				money = money - 50
				hp = hp + 2
				print(Back.GREEN)        		
				print("Здоровье увеличено на 2 ед.")
				print("У вас " + str(hp) + " здоровья")
			elif h == "0" or h == "нет" or h == "Нет":
				money = money + 0
				a = a + 0
				hp = hp + 0
				print(Back.GREEN)
				print("Урон и Здоровье не повышено")
			else:
				print(Back.MAGENTA)
				print("Вы ошиблись. С вас снято 30 монет")
				money = money - 30
				break

	# Пост-Магазин

			print("У вас " + str(money) + " монет")
			repeat = input("Хотите ли вы улучшить еще что-то?\nДа\nНет\n")
			if repeat == "Да" or repeat == "да":
				if money < 1:
					print(Back.YELLOW)
					print("У вас нет денег, вы перешли к бистве с боссом")
					break
					continue
				else:
					continue
			elif repeat == "Нет" or repeat == "нет":			
				answ = input("\nХотите ли вы сразиться с боссом?\nДа\nНет\n")
				if answ == "Да" or answ == "да":
					break
					continue
				elif answ == "Нет" or answ == "нет":
					print(Back.MAGENTA)
					print("Вы не прошли игру!")
					g = input("Хотите запустить с начала?")
					if g == "Да" or g == "да":
						break
					else: 
						print(Back.CYAN)
						print("Ошибка")
						exit(0)

		input()

###################################################################################################################################################################################################################################################

while True:

	#Легкий
	#hp = 15, урон = 1, боссов - 4.

	j = input ("Выберите режим сложности\nЛегкий\nСредний\nСложный\n")


	if j == "Легкий" or j == "легкий":
		Easy()

	#Средний
	#hp = 10, урон = 1, боссов - 5(пока не реализованно!!!), в магазине за 100 золота дают +1 урон.

	elif j == "Средний" or j == "средний":
		Midle()

	#Сложный
	#hp = 8, урон = 1, боссов - 6(пока не реализованно!!!), в магазине урон не повышается.

	elif j == "Сложный" or j == "сложный":
		Hard()

	#Ошибка!

	else:
		from colorama import init
		from colorama import Fore, Back, Style
		init()

		print(Back.MAGENTA)
		print("Вы ошиблись")

		continue
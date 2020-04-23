#Теорема Пифагора
import math


print("Нужно найти: \n 1 - Гипотенузу \n 2 - Один из катетов")


action = int((input("Только цифру: ")))

if (action == 1):
	leg1 = float(input("Длина первого катета: "))
	leg2 = float(input("Длина второго катета: "))

	hypotenuse = (leg1**2 + leg2**2) ** 0.5
	print("Без округления = " + str(hypotenuse))
	print("С округлением = " + str(round(hypotenuse)))


elif(action == 2):
	leg = float(input("Длина другого катета: "))
	hypotenuse = float(input("Длина гепотенузы: "))

	leg_ans = (hypotenuse**2 - leg**2) ** 0.5
	print("Без округления = " + str(leg_ans))
	print("С округлением = " + str(round(leg_ans)))


else:
	print("Не та цифра")




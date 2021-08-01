import random
import mymodule
from time import sleep
import sys


while True:
	succ = "чекай passes.txt в папке, где запустил пассген версии "
	print("вы хотите создать новый новый пароль или всего лишь забыли прошлый?" + "\n")

	sleep(0.5)

	otvet = input("если хотите создать новый - 1, если хотите посмотреть все пароли - 2, если хочешь выйти из петли - 3: ")

	znaki = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


	if otvet == "1":
		smisl = input("для чего нужен пароль?" + "\n")
		length = input("длина пароля?"+ "\n")
		number = int("1")
		length = int(length)
		print("Загрузка:")

		#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
		animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

		for i in range(len(animation)):
		    sleep(0.2)
		    sys.stdout.write("\r" + animation[i % len(animation)])
		    sys.stdout.flush()

		    #сделать чтобы вместо загрузки в будущем писался текст

		print("\n") 
		for n in range(number):
			password =""
			for i in range(length):
				password += random.choice(znaki)
			print()
		with open("passes.txt", "a" ) as p:
				p.write(smisl + ": " + "\n" + password + "\n")

		print("пароль успешно создан!" + "\n" + "посмотреть можно как всегда или через /2/ или в файле с названием 'passes.txt' в папке, где открыл пассген ")

		sleep(0.9)

		print("\n")
	elif otvet == "2":
		r = open("passes.txt", "r")
		read = r.read()
		print("\n" + read)
		r.close()
	elif otvet == "3":

		print("Спасибо за использование " + mymodule.__version__ + "\n"  + succ + "или через значение /2/ в консоле" )
		sleep(0.7)
		break
	else:
		print("\n" + "Ошибка, повторение операции." + "\n")
		continue
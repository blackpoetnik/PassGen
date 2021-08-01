import random
import mymodule
from time import sleep
import sys


while True:
	succ = "Check passes.txt in the folder where you run the passgen "
	print("do you want to create new one or just forgot previous?" + "\n")

	sleep(0.5)

	otvet = input("if you want to create a new one - 1, if you want to see all passwords - 2, if you want to get out of the loop - 3: ")

	znaki = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


	if otvet == "1":
		smisl = input("what the password is for?" + "\n")
		length = input("password's length?"+ "\n")
		number = int("1")
		length = int(length)
		print("Loading:")

		#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
		animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

		for i in range(len(animation)):
		    sleep(0.2)
		    sys.stdout.write("\r" + animation[i % len(animation)])
		    sys.stdout.flush()


		print("\n") 
		for n in range(number):
			password =""
			for i in range(length):
				password += random.choice(znaki)
			print()
		with open("passes.txt", "a" ) as p:
				p.write(smisl + ": " + "\n" + password + "\n")

		print("password successfully created!" + "\n" + "you can view it as usual either via /2/ or in a file called 'passes.txt' in the folder where you ran the passgen ")

		sleep(0.9)

		print("\n")
	elif otvet == "2":
		r = open("passes.txt", "r")
		read = r.read()
		print("\n" + read)
		r.close()
	elif otvet == "3":

		print("Thanks for using PassGen "+ "\n"  + succ + "or you can view it as usual either via /2/" )
		sleep(0.7)
		break
	else:
		print("\n" + "Error, repeating the operation." + "\n")
		continue
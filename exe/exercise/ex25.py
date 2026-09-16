#!/usr/bin/env python3
#猜数字游戏
import random
random_num=random.randint(1,100)
while True:
	num=int(input("Please enter a number between 1 and 100:"))
	if random_num==num:
		print("Correct!")
		break
	elif num>random_num:
		print("It's bigger than the number")
	else:
		print("It's smaller than the number")

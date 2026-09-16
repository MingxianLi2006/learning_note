#!/usr/bin/env python3
#analog atm
total=10000
password="290314"
try1=input("Please enter your password:")
while try1!=password:
	print("error!")
	try1=input("Please enter your password:")
print("Correct!")
money_get=input("How much do you want to bring back")
while int(money_get)>total:
	print("There isn't enough money")
	money_get=input("How much do you want to bring back")
balance=total-int(money_get)
print(f"you have brought back {money_get} yuan, and your balance is {balance} yuan")

#!/usr/bin/env python3
#score=int(input("Please enter your score:"))
#if score>=636:
#	print("恭喜你被南科大录取了")
account=123456
password=290314
usr_account=int(input("Please enter your account:"))
usr_password=int(input("Please enter your password:"))
if usr_account==account and usr_password==password:
	print("log in successfully!")
else:
	print("id or password is incorrect")

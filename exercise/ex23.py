#!/usr/bin/env python3
#执行登陆操作
while True:
	usr_acc=input("请输入用户名")
	usr_paw=int(input("请输入密码"))
	match usr_acc: 
		case "admin":
			if usr_paw==666888:
				print("登陆成功，进入B站首页")
				break
			else:
				print("用户名或密码错误，请重新输入")
		case "zhangsan":
			if usr_paw==123456:
				print("登陆成功，进入B站首页")
				break
			else:
				print("用户名或密码错误，请重新输入")
		case "taoge":
			if usr_paw==888666:
				print("登陆成功，进入B站首页")
				break
			else:
				print("用户名或密码错误，请重新输入")
		case "":
			print("输入的用户名或密码不能为空")
		case _:
			print("用户名或密码错误，请重新输入")

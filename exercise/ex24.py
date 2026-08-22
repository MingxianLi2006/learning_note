#!/usr/bin/env python3
while True:
	usr_name=input("请输入用户名：")
	usr_password=input("请输入密码：")
	if usr_name=="" or usr_password=="":
		print("用户名或密码不能为空，请重新输入")
		continue
	else:
		if usr_name=="admin" and usr_password=="666888":
			print("登陆成功！")
			break
		elif usr_name=="zhangsan" and usr_password=="123456":
			print("登陆成功！")
			break
		else:
			print("用户名或密码错误，请重新登陆")

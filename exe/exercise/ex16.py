#!/usr/bin/env python3
#计算电费
'''consumption=int(input("你这个月用了多少度电："))
if consumption<=2880:
	money=0.4883*consumption
	print(f"电费为{money}元")
elif consumption>2880 and consumption<=4800:
	money=0.4883*2880+(consumption-2880)*0.5383
	print(f"电费为{money}元")
else:
	money=0.4883*2880+(4800-2880)*0.5383+(consumption-4800)*0.7883
	print(f"电费为{money}元")
'''
#简易计算器
num1=float(input("Please enter the first number:"))
num2=float(input("Please enter the second number:"))
operation=input("Please enter the operation sign:")
match operation:
	case "+":
		print("The result is",num1+num2)
	case "-":
		print("The result is",num-num2)
	case "*":
		print("The result is",num1*num2)
	case "/" if num2!=0:
		print("The result is",num1/num2)
	case _:
		print("error!")


#!/usr/bin/env python3
#判断年份
year=int(input("请输入年份："))
if year%400==0 or (year%100!=0 and year%4==0):
	print("该年为闰年")
else:
	print("该年为平年")

#判断奇偶
num=int(input("Please enter a number:"))
if num%2==0:
	print(f"{num} is even")
else:
	print(f"{num} is odd")

#判断是否成年
age=int(input("Please enter your age"))
if age>=18:
	print("You are an adult")
else:
	print("You are not an adult")
#判断正负
num1=float(input("Please enter a number:"))
if num1>0:
	print(f"{num1} is positive")
elif num1<0:
	print(f"{num1} is negative")
else:
	print(f"{num1} is zero")

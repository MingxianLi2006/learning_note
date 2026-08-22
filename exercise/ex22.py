#!/usr/bin/env python3
#打印一个长为m宽为n的长方形
'''m=int(input("Please enter the length of the rectangle"))
n=int(input("Please enter the width of the rectangle"))
for i in range(m):
	for j in range(n):
		print("*",end="")
	print("\n")
#print自带换行效果 print("*",end="")可不换行
#默认end=\n
'''
#打印99乘法表
'''for i in range(1,10,1):
	for j in range(1,i+1,1):
		if j<10:
			print(f"{j}*{i}={i*j}",end="\t")
	print("\n")
'''

#画直角三角形
'''s=int(input("请输入等腰直角三角形的边长："))
for i in range(1,s+1):
	for j in range(1,i+1):
		print("*",end="")
	print("\n")
'''
#画数字金字塔
'''num=int(input("Please enter a number, then it will produce a number pyramid:"))
for i in range(1,num+1):
	for j in range(1,i+1):
		print(j,end="")
	print("\n")
'''

#打印国际象棋棋盘
for i in range(1,9):
	for j in range(1,9):
		if (i+j)%2==0:
			print("*",end="\t")
		else:
			print("#",end="\t")
	print("\n")

#!/usr/bin/env python3
'''num1=1
def fun1():
        global num1
         #修改全局变量num1
        print(num1)
fun1()  #100
print(num1)  #100
'''

'''def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y
def calc(x,y,ope):
	return ope(x,y)
operations={'+':add,'-':subtract,'*':multiply,'/':divide}
usr_input=input("请输入两个数字及运算逻辑，用逗号隔开")
parts=usr_input.split(',') #字符串的方法 拆分成列表
if len(parts) !=3:
	print("输入格式错误，请重新输入")
else:
	try:
		x=float(parts[0].strip())
		y=float(parts[1].strip())
		ope_symbol=parts[2].strip()
		if ope_symbol in operations:
			ope_func=operations[ope_symbol]
			result=calc(x,y,ope_func)
			print(f"{x}{ope_symbol}{y}={result}")
		else:
			print("不支持的运算符，请使用+-*/")
	except ValueError:
		print("请输入有效的数字")
	except ZeroDivisionError:
		print("除数不能为零")
'''
#def out_line():
#	print("-----------------------------")

out_line=lambda : print("------------------------------")
out_line()
add=lambda x,y:x+y
print(add(100,200))

data_list=['C++','C','Python','PHP','Rust']
data_list.sort()
#按字符数量排序

data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)

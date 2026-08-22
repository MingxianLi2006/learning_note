#!/usr/bin/env python3
try:
	print("===================")
#	print(my_name)
	print("abc"[10])
	print("===================")
	print(1/0)
except NameError as e:
	print("程序运行出错了，请联系管理员～：异常信息：",e)
except ZeroDivisionError as e:
	print("程序运行出错了，请联系管理员！异常信息：",e)
except IndexError as e:
	print("索引错误")
except Exception as e
#捕获所有的异常

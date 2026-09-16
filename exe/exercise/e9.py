#!/usr/bin/env python3
'''#计算n！
def factorial(x):
	if x==0:
		return 1
	while x!=0:
		return x*factorial(x-1)
print(factorial(3))
#递归
'''
#info={goods_info{"Name":...,"Price":...,"Num":...},discount{"coupon":...,"points":...},"deliver":...}
def cal_order_cost(*goods_info:tuple[str,float,int],coupon,score,express):
	'''
	:param goods_info: 商品信息（商品名、价格、数量） eg.(鼠标，188,2)(键盘，388,1)
	:param coupon:优惠券
	:param score:积分
	:param express:运费
	:return: 订单总金额
	'''
	#1.计算商品总金额
	total_price=[goods[1]*goods[2] for goods in goods_info]
	total_cost=sum(total_price)
	#列表推导式
	#2.扣减优惠券
	if total_cost>=5000 and coupon<=total_cost:
		total_cost-=coupom
	#3.扣减积分抵扣
	if total_cost>=5000 and total_cost-score//100>=0:
		total_cost-=score//100
	#4.添加运费
	total_cost+=express
	return total_cost
	#测试
total=cal_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.9)
print(total)
#可以设置优惠券积分默认=0
#tuple[]不可以用小括号，这是类型注解的规定写法

模块
多个python文件 便于管理
circle_fun.py main.py ... 在main中调用circle_fun.py的函数
Python模块 module一个.py文件就是一个模块 模块时python程序的基本组织单位。在模块中可以定义变量
函数 类 以及可执行的代码
内置模块
math random os(操作系统) sys(系统参数) datetime(日期时间) time(时间访问) re(正则) csv(csv文件操作)
eg.
#随机点名系统
import random
names=["ll","jj","qq","bb"]
print(random.choice(names))

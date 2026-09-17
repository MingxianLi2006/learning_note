#!/usr/bin/env python3
'''
class Car:
	pass

c1=Car()
#动态地为对象添加属性
c1.color="red"
c1.brand="BMW"
c1.name="X5"
c1.price=500000

print(c1.__dict__)
print(c1)
#output: <__main__.Car object at 0x000001D0A7...>
#一串数字是对象的的内存地址
'''
class Car:
        def __init__(self,c_color,c_brand,c_name,c_price):
                self.color=c_color
                self.brand=c_brand
                self.name=c_name
                self.price=c_price
        def running(self):
                print(f"{self.brand}{self.name}正在高速行驶...")
        def total_cost(self,discount,rate):
                return self.price*discount+self.price*rate
c1=Car("Red","BMW","X5",50000)
total_cost=c1.total_cost(0.9,0.1)
print(f"提车总价为：{total_cost:.0f}")

c1.running()

#!/usr/bin/env python3
'''s=[56,90,88,65,90,101]
print(type(s))
print(s[0])
print(s[-6])
print(s[5])
s[5]=100
print(s[5])
print(s)
del s[0]
print(s)
print(s[0:5:2])
print(s[-1:-5:-1])
s.append(1928)
print(s)
s.insert(0,98)
print(s)
s.reverse()
print(s)
s.sort()
print(s)
'''
s=[]
#定义一个空列表
for i in range(10):
	s[i-1]=int(input("Please enter a number:"))
'''用	num-int(input("Please enter a number"))
	s.append(num)
'''
s.sort()
print(f"最小值为{s[0]}")
print(f"最大值为{s[9]}")
sum=0
for j in range(10):
	sum+=s[j-1]
avg=sum/10
print(f"平均值为{avg}")
#sum(s)对列表求和 len(s)获取元素个数/列表长度

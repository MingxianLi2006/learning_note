#!/usr/bin/env python3
'''
#将多个列表合并去除重复元素升序输出
list1=['M','A','C','E','F','G','H','L','N','I','J','K','O']
list2=['X','Z','T','Y','D','E','F','G']
list3=['W','A','S','D']
new_list=list1+list2+list3
list4=[]
for i in new_list:
	if i not in list4:
		list4.append(i)
list4.sort()
print(list4)
'''

'''
#将下表中能被3或者5整除的元素提取出来，获取这些数字对应的平方，组成一个新列表
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
list2=[]
for i in list1:
	if i%3==0 or i%5==0:
		list2.append(i**2)
print(list2)
'''

#将如下列表的正数提取出来，封装为一个新的列表
list1=[11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
list2=[]
for i in list1:
	if i>0:
		list2.append(i)
print(list2)

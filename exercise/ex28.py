#!/usr/bin/env python3
#合并两个列表的元素 去除重复元素
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]
'''
for i in range(9):
	num_list1.append(num_list2[i])
num_list1.sort()
print(num_list1)
j=0
while j<len(num_list1):
	if num_list1[j]==num_list1[j+1]:
		num_list1.pop(j)
	j+=1
print(num_list1)
'''
for num in num_list2:
	num_list1.append(num)
print("合并后的原始列表",num_list1)
new_list=[]
for num in num_list1:
	if num not in new_list:
#in存在返回True
		new_list.append(num)
print(new_list)

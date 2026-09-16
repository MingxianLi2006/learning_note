#!/usr/bin/env python3
list1=[]
for i in range(1,21,1):
	list1.append(i**2)
print(list1)
list2=[19,23,54,64,87,20,109,232,123,43,26,55,72]
list3=[]
k=0
for j in range(len(list2)):
	if list2[j]%2==0:
		list3.append(list2[j]**2)
print(list3)

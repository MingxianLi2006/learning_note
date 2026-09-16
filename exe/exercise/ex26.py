#!/usr/bin/env python3
total=0
for i in range(1,1001):
	if(i%5==0):
		total+=i
print(f"sum is {total}")
s="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
num1=0
num2=0
for j in s:
	if j=="a":
		num1+=1
	if j=="k":
		num2+=1
print(f"There are totally {num1} a and {num2} k in the string")

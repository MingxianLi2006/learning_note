#!/usr/bin/env python3
total1=total2=0
for i in range(1,101,1):
	if i%2!=0:
		total1+=i
for j in range(100,501,1):
	if j%3==0:
		total2+=j
print(total1)
print(total2)

#!/usr/bin/env python3
a=int(input("Please enter the first side of the triangle"))
b=int(input("Please enter the second side of the triangle"))
c=int(input("Please enter the third side of the triangle"))
if a+b<=c or a+c<=b or b+c<=a:
	print("These three side can not form a triangle")
elif a==b==c:
	print("This is an 等边三角形")
elif a==b or b==c or a==c:
	print("This is an 等腰三角形")
else:
	print("This is an common triangle")

#!/usr/bin/env python3
acc1="admin"
paw1=666888
acc2="root"
paw2=547527
acc3="zhangsan"
paw=123456
usr_acc=input("Please enter your account:")
usr_paw=int(input("Please enter your password:"))
if usr_acc==acc1 and usr_paw==paw1:
	print("log in successfully!")
elif usr_acc==acc2 and usr_paw==paw2:
	print("s")
else:
	print("log in unsuccessfully")

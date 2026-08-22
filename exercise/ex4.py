#!/usr/bin/env python3
dict1={"wl":670,"hl":556,"lmw":582,"zl":435,"xlg":608,"wz":512,"zz":678}
print(dict1)
#if "wl":700 added to the tail of the dictionary "wl":700 will be printed out
#data was overlapped
#int can be key    tuple cam be key   list cannot be key
#as key cannot be modified
print(dict1["lmw"])
#to access the value of "lmw"
dict1["lmw"]=688
#modify the value
print(dict1["lmw"])

dict1["tg"]=700
print(f"add {dict1}")
score_of_zz=dict1.pop("zz")
print(f"score of zz is {score_of_zz}")
print(f"delete {dict1}")
del dict1["wz"]
print(dict1)

#遍历
for k in dict1.keys():
	print(f"{k}:{dict1[k]}")
for item in dict1.items():
	print(f"{item[0]}:{item[1]}")
#解包
for k,v in dict1.items():
	print(f"{k}:{v}")
	

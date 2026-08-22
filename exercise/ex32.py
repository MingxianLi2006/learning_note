#!/usr/bin/env python3
'''s="Hello-Python-Hello-World"
index1=s.find("H")
index2=s.find("Python")
print(index1,index2)

su=s.upper()
print(s)
print(su)
sq=s.split('o')
print(sq)
s2=s.split('l')
print(s2)
'''

#检验邮箱格式是否正确
'''email=input("Please enter your email:")
cot1=email.count('@')
cot2=email.count('.')
if cot1==1 and cot2>=1:
	print("Correct email form")
else:
	print("Wrong email form")
#.的检验可替换为"." in email
print(len(email))
'''

#输入一个字符串判断是否回文
'''string1=input("Please enter a string:")
exp=True
for i in range(0,len(string1)//2,1):
	if string1[i]!=string1[len(string1)-i-1]:
		exp=False
		break
	else:
		exp=True
if exp:
	print("该字符串是回文")
else:
	print("该字符串不是回文")
'''
#将用户输入的十个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容遍历输出
strings=[]
for i in range(10):
	s=input(f"请输入第{i+1}个字符串")
	s1=s[::-1]
#字符串反转靠切片
	s1.upper()
	strings.append(s1)
for j in range(10):
	print(strings[j])

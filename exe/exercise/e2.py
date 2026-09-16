#!/usr/bin/env python3
#两个变量 交换然后输出
'''
a=10
b=20
print(a,b)
t1=a,b
b,a=t1
print(a,b)
'''
'''
a=100
b=200
c=300
t2=a,b,c
print(a,b,c)
c,a,b=t2
print(a,b,c)
#a,b=b,a也行
'''
stu_id=("s001","s002","s003","s004","s005","s006","s007","s008","s009","s010")
stu_name=("wl","lmw","ss","zn","zt","wz","hd","xlg","xm","tt")
stu_ch_score=(85,92,78,88,95,76,89,75,86,66)
stu_math_score=(92,88,85,79,96,82,91,69,89,59)
stu_en_score=(78,95,82,91,89,77,94,82,98,72)
total_score=[]
avg_score=[]
for i in range(10):
	total_score.append(stu_ch_score[i]+stu_math_score[i]+stu_en_score[i])
	print(f"{stu_id[i]},{stu_name[i]}'s total score is {total_score[i]}\t")
'''ch_avg_score=sum(stu_ch_score)/10
math_avg_score=sum(stu_math_score)/10
en_avg_score=sum(stu_en_score)/10
print(f"Chisnese average score is {ch_avg_score}")
print(f"Maths average score is {math_avg_score}")
print(f"English average score is {en_avg_score}")
'''
avg_score=[sum(stu_ch_score)/10,sum(stu_math_score)/10,sum(stu_en_score)/10]
print(f"Chisnese average score is {avg_score[0]}")
print(f"Maths average score is {avg_score[1]}")
print(f"English average score is {avg_score[2]}")
max_score=[max(stu_ch_score),max(stu_math_score),max(stu_en_score)]
min_score=[min(stu_ch_score),min(stu_math_score),min(stu_en_score)]
print(f"Chinese highest score is {max_score[0]}, lowest score is {min_score[0]}")
print(f"Maths highest score is {max_score[1]}, lowest score is {min_score[1]}")
print(f"English highest score is {max_score[2]}, lowest score is {min_score[2]}")
for j in range(10):
	if total_score[j]>270:
		print(f"{stu_id[j]} {stu_name[j]} is excellent!")
for k in range(10):
	if total_score[k]<250:
		print(f"{stu_id[k]} {stu_name[k]} is rubbish")
'''
也可以元组套元组
students=(("S001","wl",85,92,78),("S002","lmj",92,88,95))
for s in students:
	total=s[2]+s[3]+s[4]
	avg=total/3
	print(f"{s[0]} {s[1]} 's total score is {total}")
chinese_scores=[s[2] for s in students]
'''
#如果科目变多 那么代码可读性会下降（s[1]这种太多了） 可用解包
'''
for id,name,chinese,math,english in students:
	total=chinese+math+english
	avg=total/3
	print(f{id})
'''

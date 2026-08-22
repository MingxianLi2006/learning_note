#!/usr/bin/env python3
#开发教务系统
menu='''
#1.添加学生信息\t2.修改学生信息\t3.删除学生信息\t4.查询学生信息\t5.列出所有学生\t6.统计班级成绩\t7.退出系统
##########################################################################################################
'''
stu_info={}
while True:
	print(menu)
	ope=input("请选择要执行的操作（1-7）：")
	match ope:
		case "1":
			stu_id=input("请输入学生姓名：")
			if stu_id in stu_info.keys():
				print("学生已存在，请重新输入！")
			else:
				ch_score=int(input("请输入语文成绩："))
				math_score=int(input("请输入数学成绩："))
				en_score=int(input("请输入英语成绩："))
				stu_info[stu_id]={"语文成绩":ch_score,"数学成绩":math_score,"英语成绩":en_score}
				print(f"添加【{stu_id}】成功")
		case "2":
			stu_id=input("请输入学生姓名：")
			if stu_id not in stu_info.keys():
				print("学生不存在，请重新输入！")
			else:
				ch_score=int(input("请输入语文成绩："))
				math_score=int(input("请输入数学成绩："))
				en_score=int(input("请输入英语成绩："))
				stu_info[stu_id]={"语文成绩":ch_score,"数学成绩":math_score,"英语成绩":en_score}
				print(f"修改【{stu_id}】成功")

		case "3":
			stu_id=input("请输入学生姓名：")
			if stu_id not in stu_info.keys():
				print("学生不存在，请重新输入")
			else:
				del stu_info[stu_id]
		case "4":
			stu_id=input("请输入学生姓名：")
			if stu_id not in stu_info.keys():
				print("学生不存在，请重新输入")
			else:
				print(f"学生姓名：{stu_id}\t语文成绩：{stu_info[stu_id]['语文成绩']}\t数学成绩：{stu_info[stu_id]['数学成绩']}\t英语成绩：{stu_info[stu_id]['英语成绩']}")
		case "5":
			print("姓名\t语文成绩\t数学成绩\t英语成绩")
			for st_id,st_score in stu_info.items():
				print(f"{st_id}\t{st_score['语文成绩']}\t\t{st_score['数学成绩']}\t\t{st_score['英语成绩']}")
		case "6":
			ch_score=[]
			math_score=[]
			en_score=[]
			for st_id,st_score in stu_info.items():
				ch_score.append(st_score['语文成绩'])
				math_score.append(st_score['数学成绩'])
				en_score.append(st_score['英语成绩'])
			max_ch_score=max(ch_score)
			max_math_score=max(math_score)
			max_en_score=max(en_score)
			min_ch_score=min(ch_score)
			min_math_score=min(math_score)
			min_en_score=min(en_score)
			avg_ch_score=sum(ch_score)/len(stu_info.keys())
			avg_math_score=sum(math_score)/len(stu_info.keys())
			avg_en_score=sum(en_score)/len(stu_info.keys())
			print(f"班级语文成绩的最高分为：{max_ch_score}，最低分为{min_ch_score}，平均分为{avg_ch_score:.1f}")
			print(f"班级数学成绩的最高分为：{max_math_score}，最低分为{min_math_score}，平均分为{avg_math_score:.1f}")
			print(f"班级英语成绩的最高分为：{max_en_score}，最低分为{min_en_score}，平均分为{avg_en_score:.1f}")
			print("班级语文最高分的同学为:",end="")
			for st_id,st_score in stu_info.items():
				if st_score['语文成绩']==max_ch_score:
					print(f"{st_id}",end=" ")
			print("班级语文最低分的同学为:",end="")
			for st_id,st_score in stu_info.items():
				if st_score['语文成绩']==min_ch_score:
					print(f"{st_id}",end=" ")
			print("\n")
			print("班级数学最高分的同学为:",end="")
			for st_id,st_score in stu_info.items():
                	        if st_score['数学成绩']==max_math_score:
                	                print(f"{st_id}",end=" ")
			print("班级数学最低分的同学为:",end="")
			for st_id,st_score in stu_info.items():
				if st_score['数学成绩']==min_math_score:
					print(f"{st_id}",end=" ")
			print("\n")
			print("班级英语最高分的同学为:",end="")
			for st_id,st_score in stu_info.items():
				if st_score['英语成绩']==max_en_score:
					print(f"{st_id}",end=" ")
			print("班级英语最低分的同学为:",end="")
			for st_id,st_score in stu_info.items():
				if st_score['英语成绩']==min_en_score:
					print(f"{st_id}",end=" ")
			print("\n")
		case "7":
			print("系统已退出")
			break
		case _:
			print("错误输入！请重新输入")


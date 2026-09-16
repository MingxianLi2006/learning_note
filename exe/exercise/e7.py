#!/usr/bin/env python3
'''def circle_area_len(r):
	circle_area=3.14*r*r
	circle_len=3.14*r*2
	return circle_area,circle_len
print(circle_area_len(3))
a,b=circle_area_len(3)
print(f"{a},{b}")

'''
def triangle_area(base,height):
	'''
	The function use base * height / 2 to calculate area of the triangle
	:param base: the base of the triangle
	:param height: the height of the triangle
	:return: the area of the triangle
	'''
	area=base*height/2
	return area
def vowel_counting(string):
	'''
	The function is used to calculate the number of vowel in a string
	:param string: the string that user enter
	:param i: used in the loop to counts the vowel one by one
	:param j: used in the loop to refer to each grapheme
	:vovels :the set of vowels
	:return: the number of vowel in a string
	'''
	vowels={'a','e','i','o','u','A','E','I','O','U'}
	i=0
	for j in string:
		if j in vowels:
			i+=1
	return i

def max_min_average_score(score_list):
	'''
	The function is used to find the highest, lowest, average scores in the list
	:param score_list: the score list that user uploaded
	'''
	max_score=max(score_list)
	min_score=min(score_list)
	avg_score=round(sum(score_list)/len(score_list),1)
	return max_score,min_score,avg_score

def score_to_level(score):
	if score>=90:
		return 'A'
	elif score>=75:
		return 'B'
	elif score>=60:
		return 'C'
	else:
		return 'D'
def circle_string_yes_or_no(string):
	result=True
	for i in range(len(string)):
		if string[i]!=string[len(string)-i-1]:
			result=False
	return result

def seconds_to_hour_minute_second(second):
	minute=second//60
	hour=minute//60
	second=second%60
	minute=minute%60
	return hour,minute,second
def type_of_triangle(first_side,second_side,third_side):
	if first_side+second_side<third_side or first_side+third_side<second_side or second_side+third_side<first_side:
		print("这三条边无法构成三角形")
	else:
		if first_side==second_side or first_side==third_side or second_side==third_side:
			if first_side==second_side==third_side:
				print("该三角形为等边三角形")
			else:
				print("该三角形为等腰三角形")
		else:
			print("该三角形为普通三角形")
	

print("底长为30,高度为20的三角形面积为：",triangle_area(30,20))
str=input("请输入一个字符串：")
print(f"The number of the vowels in that string is {vowel_counting(str)}")
list1=input("请输入学生的高考成绩列表")
max_score,min_score,avg_score=max_min_average_score(list1)
print(f"最高分：{max_score},最低分：{min_score},平均分：{avg_score}")
#input输入的是大字符串""

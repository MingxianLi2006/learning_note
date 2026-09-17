#!/usr/bin/env python3
'''s1={5,3,2,0,9,12,43,64,22,5,0}
print(s1)
s1.add(1200)
print(s1)
s1.clear()
print(s1)
'''
football_set={"wl","zn","xlg","dt","tyz","hl","lfy","wc","zl"}
basketball_set={"zt","mjr","wl","jld","zn","wc","hl","tyz","lhy","lfy","yl"}
french_set={"xm","wz","ss","hp","jld","tyz","hd","lfy","hl","zn"}
art_set={"dt","tyz","hl","hp","jld","zl"}
print(f"同时选修了法语和艺术的学生：{french_set.intersection(art_set)}")
print(f"同时选修了所有四门课程的学生：{(football_set.intersection(art_set)).intersection(football_set.intersection(basketball_set))}")
print(f"选修了足球但没选修篮球的学生：{football_set.difference(basketball_set)}")
all_set=(football_set.union(basketball_set)).union(french_set.union(art_set))
for i in all_set:
	j=0
	if i in football_set:
		j+=1
	if i in basketball_set:
		j+=1
	if i in french_set:
		j+=1
	if i in art_set:
		j+=1
	print(f"{i}选修了{j}门课程\t")

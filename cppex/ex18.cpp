#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
struct stu
{
	string name;
	int age;
};
bool cmp(stu a, stu b)
{
	if(a.age!=b.age)
		return a.age<b.age;
	else
		return a.name<b.name;
}
//年龄不相等从小到大排序 否则按照名字的字典序
int main(){
	stu s[3];
	for(int i=0;i<3;i++)
		cin>>s[i].name>>s[i].age;
//tom 19
//mike 20
//tt 12

	sort(s,s+3,cmp);
	for(int i=0;i<3;i++)
		cout<<s[i].name<<" "<<s[i].age<<endl;

	return 0;
}

#include <iostream>
#include <vector>
using namespace std;
int main(){
	vector <int> v(10,2);
//分配了10个空间 每个空间都初始化为2
	for(int i=0;i<10;i++)
	cout<<v[i]<<" ";
	cout<<endl;
	v.resize(2);
//resize后只有多出来的空间会变成0 如果旧大小>=新大小 则只改变空间不改变值
	for(int k=0;k<2;k++)
        cout<<v[k]<<" ";
        cout<<endl;

	vector <int> u(10);
//分配了十个空间全都初始化为0
	for(int j=0;j<10;j++)
	cout<<u[j]<<" ";
	cout<<endl;
//遍历一遍 不考虑开头与结束
	v.push_back(12);
	for(auto p=v.begin();p!=v.end();p++)
//v.end()指向最后一个元素后面
	cout <<*p<<" ";
	cout<<endl;
}

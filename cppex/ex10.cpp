//set集合元素互不相同 元素会按照从小到大排序
//插入遍历查找删除
#include<iostream>
#include<set>
#include<vector>
using namespace std;

int main(){
	set <int> s;
//不可加参数 分配空间也不可行
//	vector <int> v(10,2);

//插入元素
	s.insert(4);
	s.insert(2);
	s.insert(1);
	for(auto p=s.begin();p!=s.end();p++)
		cout<<*p<<" ";
//读取指针指的元素
	cout<<endl;
//输出1 2 4

//查找
	cout<<(s.find(2)!=s.end())<<endl;
	cout<<(s.find(5)!=s.end())<<endl;
//分别输出1 0表示true false
//	加了括号是布尔值
//	s.find()的返回值是指针
//s.find执行一次查找 找到了就返回所找元素的迭代器 没找到就返回s.end()（末尾迭代器）

//删除元素
	s.erase(1);
	cout<<(s.find(1)!=s.end())<<endl;
//输出0表示false
return 0;
}

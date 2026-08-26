//栈只允许在表的一段进行插入、删除操作的线性表
//有口无肛门
//栈stack先进后出 queue队列先进先出
//创建栈stack <元素类型> s
//处理 压栈 出栈 访问栈顶 获取长度
#include<iostream>
#include<stack>
using namespace std;
int main(){
//创建栈
	stack <int> s;
//压栈
	s.push(1);
	s.push(2);
	s.push(3);
//先放1 再放2、 3
	cout << s.top() <<endl;
//输出栈顶3

//出栈
	s.pop();
	cout<<s.top()<<endl;
//输出2

//获取长度
	cout << "栈的长度为："<<s.size()<<endl;
//遍历不可行 栈没有begin 方法 无法获取除了栈顶外的元素
//	for(auto p=s.begin();p!=s.end();p++)
//		cout<<*p<<endl;
return 0;
}

//c++11的解释 新增 auto to_string() stoi stof unordered_map unordered_set
#include<iostream>
#include<vector>
using namespace std;
int main(){
//auto声明
//auto x=19;自动识别数据类型
//auto float y=1.8;
//不可
//auto a;
//cin>>a;
//需要直接初始化
//不过可以cin>>n;  auto a=n;

//迭代器
vector <int> a(10,1);
for(auto p=a.begin();p!=a.end();a++)
	cout<<*p<<" ";
return 0;
}
//数组可用迭代器
//集合可用
//键值对遍历可用 获取值时类似结构体指针
//栈只可访问栈顶 队列只可访问队首队尾 不可用
//unordered也可

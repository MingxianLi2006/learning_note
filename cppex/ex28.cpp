#include<iostream>
using namespace std;
int main()
{
//	char *s="hello";
//	cout<<s<<endl;	//hello
//	cout<<*s<<endl;//h 解引用 会输出地址存放的字符 s存放的是首地址

//弃用写法
//可用 const char *s="hello";
	char name1[]="SUSTech";
	char name2[]="SUST" "ech";
	cout<<&name1<<endl;
	cout<<name2<<endl;
	cout<<name1[]<<endl;
	return 0;
}

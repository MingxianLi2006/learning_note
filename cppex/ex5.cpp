#include <iostream>
using namespace std;
int main(){
	string s ="hello";
	string s2="world";
	string s3=s+s2;
	string s4;
	getline(cin,s4);//获取一行
	cout<<s3<<endl;
	cout<<s4<<endl;
	cout<<s.length()<<endl;
	cout<<s4.length()<<endl;
	string s_sub=s.substr(1,2);
	cout << s_sub<<endl;
	//substr(1,2)从第[1]个字符开始数 输出两个字符组成的子字符串
	//0才是第一个字符
	return 0;
}

//cin只能获取单个单词 换行回车都视为结束
//s.length()计算长度 是字符串的方法
//空格长度为1

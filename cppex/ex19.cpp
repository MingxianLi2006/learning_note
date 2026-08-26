#include<cctype>
//C语言的#include<ctype.h>
#include<iostream>
using namespace std;
int main(){
	char c = 'A';

cout<<"isalpha:"<<isalpha(c)<<endl;//判断是否是字母
cout<<"islower:"<<islower(c)<<endl;//判断是否小写字母
cout<<"isupper:"<<isupper(c)<<endl;//判断是否大写字母
cout<<"isalnum:"<<isalnum(c)<<endl;//判断是否是字母or数字
cout<<"isspace:"<<isspace(c)<<endl;//判断是否是空格 \t \r \n
//布尔类型
//其实是int类型 但是可以将非0理解为true 理解为false就行了
char s=tolower(c);//转化成小写字母
cout<<s<<endl;
char s1=toupper(c);
cout<<s1<<endl;
return 0;

}

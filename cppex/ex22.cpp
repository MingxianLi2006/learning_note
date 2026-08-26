//to_string 将数字转化成字符变量
#include<iostream>
#include<string>
using namespace std;
int main(){
string s=to_string(19);
cout<<s<<endl;
printf("%s\n",s.c_str());
return 0;
}

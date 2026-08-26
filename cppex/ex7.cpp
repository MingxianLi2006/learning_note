//引用和传址
#include<iostream>
using namespace std;
void c(int &a)
{a+=1;
}
//定义了一个函数
//c++的引用和c的取地址符号没有关系
int main(){
int a=4;
c(a);
cout<<a<<endl;
return 0;
}
//这里&是引用会改变函数值，如果去掉则不会改变

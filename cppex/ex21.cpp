#include<iostream>
#include<vector>
using namespace std;
//基于范围的for 循环
//传值 for(int i:arr) cout<<i<<endl;   输出数组中的每一个元素的值 不能改变元素的值
//传址 for(int &i:arr) i=i*2;               将数组中的每一个元素都*2 只有在引用的时候才能改变元素的值
//推广 for(auto i:v) cout<<i<<" ";       这里的v是一个vector其实所有的容器都可以使用这种方式循环（配合auto）

int main(){
	int a[5]={1};//1 0 0 0 0
	for(int i:a)//用i访问a
		cout<<i<<" ";
//输出a[i]   有点像python 的for i in a
	cout<<endl;

	for(int i:a)
		i++;

	for(int i:a)
		cout<<i<<" ";
//1 0 0 0 0
//传值调用 不改变值
	cout<<endl;
	
	int b[5]={1};
	for(int &i:b)
		i++;
	for(int i:b)
		cout<<i<<" ";

//传址调用


	vector <int> c(10,1);
	for(auto i:c)//改int也可正常输出
		cout<<i<<" "
return 0;
}

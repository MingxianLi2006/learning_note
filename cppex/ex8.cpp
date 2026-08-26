//stl篇stl是Standard Template Library标准模板库 是C++标准库的核心组成部分
//本质上是一套数据结构与算法的工具箱
//vector 动态大小 可以随意增删元素的数组替代品 向量
//在<vector>里面 
//vector <int> v; 空数组

#include<vector>
#include<iostream>
using namespace std;
int main(){
	vector <int> v; 
//空数组

//分配数组大小v.resize(length)
	v.resize(10);
	cout<<v.size()<<endl;
//显示大小
	for(int i=0;i<10;i++){
		v[i]=i;}
	for(int j=0;j<10;j++){
		cout<<v[j]<<" ";}
//遍历赋值 输出

//追加元素
	v.push_back(11);
	for(int k=0;k<11;k++) 
		cout<<v[k]<<" ";
//将11放入v并且添加空间
	return 0;
}

//sort()函数
//主要功能是对一个数组int arr[] 或者 vector进行排序 vector是容器 需要用begin end表示头尾
//arr[]使用 arr表示数组首地址 arr+n表示尾部
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	vector <int> m(10);
	for(int i=9;i>=0;i--)
		m[i]=10-i;
	for(int k=0;k<10;k++)
		cout<<m[k]<<" ";
	cout<<endl;
	m.push_back(-1);
	sort(m.begin(),m.end());
//sort(开始排序的地方,结束排序的地方,cmp) 不一定是头尾 可以是中间部分排序
//从小到大排序
	for(int j=0;j<11;j++)
		cout<<m[j]<<" ";
	cout<<endl;
//sort()默认从小到大排序 但是使用cmp可以自定义一些规则compare

}

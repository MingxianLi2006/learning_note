//sort()默认从小到大排序 但是使用cmp可以自定义一些规则compare

#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
bool cmp(int x,int y){
	return x>y;
}
//bool 类型函数 如果返回true x排在y前面 如果返回false y排在x前面
//不能有等于
int main(){
	vector <int> v;
	for(int i=1;i<=10;i++)
		v.push_back(11-i);
	for(auto p=v.begin();p!=v.end();p++)
		cout<<*p<<" ";
	cout<<endl;
//从大到小push进去
        	sort(v.begin(),v.end());

        	for(auto p=v.begin();p!=v.end();p++)
                	cout<<*p<<" ";
        	cout<<endl;
//从小到大
//使用cmp

		sort(v.begin(),v.end(),cmp);
		for(int i=0;i<10;i++)
		cout<<v[i]<<" ";
		cout<<endl;

return 0;
}
//在sort内部如果cmp为真 则顺序不变 如果为假 则交换

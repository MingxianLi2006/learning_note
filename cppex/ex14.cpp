//unordered_map unordered_set
//无序map set 省去了排序的过程 如果刷题的时候超时了 可以使用
//操作和有序的相同
#include<iostream>
#include<unordered_map>
#include<unordered_set>
using namespace std;
int main(){
	unordered_map <string,int> m;
	unordered_set <int> s;
	s.insert(1);
	s.insert(2);
	s.insert(3);

	m["hello"]=1;
	m["world"]=2;
	m["fuck"]=3;
	cout<<"集合中的元素为：";
	for(auto p=s.begin();p!=s.end();p++)
		cout<<*p<<" ";
	cout<<endl;
	for(auto p=m.begin();p!=m.end();p++){
		cout<<"key:"<<p->first<<" value:"<<p->second<<" ";
		cout<<endl;}

return 0;
}
//输出顺序和哈希表有关

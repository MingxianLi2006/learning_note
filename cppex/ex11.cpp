//map键值对 它会自动将所有键值对按照键从小到大（ASCII）排序
//创建键值对eg. map <string,int> m;
//添加 访问 遍历 获取长度
#include<iostream>
#include<map>
using namespace std;
int main(){
	map <string,int> m;
//添加
	m["hello"]=2;
	m["fuckyou"]=3;
//访问
	cout<<"hello: "<<m["hello"]<<endl;
//遍历：迭代器 获取值时类似的结构性指针
	for(auto p=m.begin();p!=m.end();p++)
		cout<<p->first<<":"<<p->second<<endl;
//m.begin()是结构体指针
/*类似这种
struct m
{
	string key;
	int data;
};
*/
//获取长度 m.size()  stack queue 都可以获得长度
	cout<<"the length of map:"<<m.size()<<endl;
//输出键的个数
return 0;
}

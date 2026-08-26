//队列 有口有肛门 先进先出
#include <queue>
#include <iostream>
using namespace std;
int main(){
	queue <int> q;
//入队
	for(int i=1;i<=10;i++)
		q.push(i);
//可获取队首队尾元素
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

//出队
	q.pop();
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

	q.push(11);
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

//获取长度
	cout<<q.size()<<endl;
return 0;
}

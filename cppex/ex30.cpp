#include<iostream>
using namespace std;
template<typename T>
T sum(T x,T y)
{
	cout<<"The input type is "<<typeid(T).name()<<endl;
	return x+y;
}
struct Point
{
	int x;
	int y;
};
template<>
Point sum<Point>(Point pt1,Point pt2)
{
	cout<<"The input type is "<<typeid(pt1).name()<<endl;
	Point pt;
	pt.x=pt1.x+pt2.x;
	pt.y=pt1.y+pt2.y;
	return pt;
}
int main()
{
	cout<<sum(1,2)<<endl;
	Point p1={1,5};
	Point p2={2,4};
	Point pt=sum(p1,p2);
	cout<<"pt=("<<pt.x<<","<<pt.y<<")"<<endl;
	return 0;
}

#include<iostream>
#include<cmath>
using namespace std;
float norm_l1(float x,float y)
{
	float l1;
	l1=abs(x)+abs(y);
	return l1;
}
float norm_l2(float x,float y)
{
	float l2;
	l2=sqrt(x*x+y*y);
	return l2;
}
float (*norm_ptr)(float,float)=norm_l1;
int main()
{
	cout<<"l1 norm of (-3.0,4.0) is "<<norm_ptr(-3.0f,4.0f)<<endl;
	norm_ptr=&norm_l2;
	cout<<"l2 norm of (-3.0,4.0) is "<<(norm_ptr)(-3.0f,4.0f)<<endl;

	return 0;
}

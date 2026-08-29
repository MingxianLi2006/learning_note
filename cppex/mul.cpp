#include <iostream>
using namespace std;
int mul(int a,int b)
{
	return a*b;
}
int main()
{
	int a,b;
	cout << "Please enter two numbers"<<endl;
	cin >> a;
	cin >> b;
	cout <<"the result of the calculation is" << mul(a,b)<<endl;

	return 0;
}

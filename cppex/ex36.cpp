#include<iostream>
using namespace std;
int main()
{
	int n,fa;
	do{	
		cout<<fa<<" "<<n<<endl;
		fa*=n;
		n++;

	}while(n<=10);
	cout<<"fa= "<<fa<<endl;
	return 0;
}

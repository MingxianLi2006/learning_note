#include<iostream>
using namespace std;
void div2(double val)
{
        cout<<"Entering val= "<<val<<endl;
        if(val>1.0)
                div2(val/2);//function call itself
        else
                cout<<"-----------------"<<endl;
        cout<<"Leaving val="<<val<<endl;
}

int main()
{
	div2(19.2);
	return 0;
}

//stop stod string to int     string to double
#include<iostream>
#include<string>
using namespace std;
int main(){
int a=stoi("123");
cout<<a-1<<endl;
double b=stod("12.34");
cout<<b-1<<endl;
printf("%f",b);


return 0;
}
//还有stof stold stol stoll stoul stoull

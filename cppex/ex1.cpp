#include <iostream>
//input and output stream
using namespace std;
//使用std名称空间  封装了函数cin cout等
int main()
{
	int n;
	cin >> n;
//cin ->scanf  scanf("%d",&n)
	cout << "I am so handsome" << n++ << endl;
//	cout << "Hello world" << endl;
//endl 换行 "\n"

	return 0;
}
/*
如果去除了using namespace std;
则下面要改成
std::cin>>n
std::cout<<I am so handsome<<n++<<std::endl;
*/
//cin cout运算速度不如scanf print
//使用c中的头文件 去除.h加c
//include <cstring>
//include <cmath>

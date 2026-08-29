#include<stdio.h>
int main(){
	const int a = 10;
	int *p=&a;
	*p=50;
	printf("%d",a);




	return 0;
}

#include<iostream>
using namespace std;
int main()
{
	FILE *fp=fopen("lab1.txt","w");
	//FILE指针 打开并且命名一个文档为lab1.txt 进行写入w操作
	if(fp==NULL)
	{
	printf("无法创建文件");
	return 1;
	}

	fprintf(fp,"第一行");
	fprintf(fp,"第二行");

	fclose(fp);
	printf("写入成功！");
	return 0;
}

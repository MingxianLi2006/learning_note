#include<stdio.h>
#include<stdlib.h>
//定义节点结构体
typedef struct Node{
	int data;
	struct Node* next;
}Node;

//创建新节点的函数
Node* createNode(int value){
	Node* newNode=(Node*)malloc(sizeof(Node));
	if (newNode==NULL){
	printf("内存分配失败！\n");
	exit(1);}
	newNode->data=value;
	newNode->next=NULL;
	return newNode;
}
int main(){
	//创建一个节点
	Node* head=createNode(42);
	//打印节点信息
	printf("节点地址：%p\n",head);
	printf("节点数据：%d\n",head->data);
	printf("下一个节点：%p\n",head->next);

	//释放内存
	free(head);

	return 0;}

#include<cfloat>
#include<iostream>
using namespace std;
struct Matrix
{
	int rows;
	int columns;
	float* pData;
};
float Matrix_Max(const Matrix& mat)//引用
{
	float maximum=FLT_MIN;
	for(int i=0;i<mat.rows;i++)
	{	for(int j=0;j<mat.columns;j++)
		{
			maximum=(maximum>mat.pData[mat.columns*i+j])?maximum:mat.pData[mat.columns*i+j];
		}
	}
	return maximum;
}
int main()
{
	cout<<1<<endl;
	Matrix mata={3,4};
	cout<<2<<endl;
	mata.pData=new float[mata.rows*mata.columns]{1.0f,2.0f,4.0f,8.0f,5.0f,6.0f,7.0f,19.0f,20.0f,50.0f,80.0f,9.0f};
	//申请地址存放拷贝数据   原始数据在可执行程序里面
	//mata.pData获得了拷贝数据的首地址
	//函数获得了mata的地址 从而找到了pData这个成员变量自身在栈上的地址 之后读取了pData里存的值 堆的首地址 从而通过这个去堆上访问数据
	cout<<3<<endl;
	float maxa=Matrix_Max(mata);
	cout<<4<<endl;
	cout<<"The maximum element of matrix a is "<<maxa<<endl;
	cout<<5<<endl;
	delete[] mata.pData;
	return 0;
}



#include <cfloat>
#include <iostream>
using namespace std;

struct Matrix {
    int rows;
    int columns;
    float* pData;
};

// 指针版本：传指针
float Matrix_Max(const Matrix* mat) {  // ← 改成指针
    float maximum = FLT_MIN;
    for (int i = 0; i < mat->rows; i++) {        // ← 用 ->
        for (int j = 0; j < mat->columns; j++) {  // ← 用 ->
            float val = mat->pData[mat->columns * i + j];  // ← 用 ->
            maximum = (maximum > val) ? maximum : val;
        }
    }
    return maximum;
}

int main() {
    cout << 1 << endl;
    Matrix mata = {3, 4};
    cout << 2 << endl;
    mata.pData = new float[mata.rows * mata.columns]{
        1.0f, 2.0f, 4.0f, 8.0f,
        5.0f, 6.0f, 7.0f, 19.0f,
        20.0f, 50.0f, 80.0f, 9.0f
    };
    cout << 3 << endl;
    float maxa = Matrix_Max(&mata);  // ← 传地址（取地址符 &）
    cout << 4 << endl;
    cout << "The maximum element of matrix a is " << maxa << endl;
    cout << 5 << endl;
    delete[] mata.pData;
    return 0;
}
指针版本

也可以直接传结构体
保证函数的健壮性 检查输入 如果pData是NULL 则会报错

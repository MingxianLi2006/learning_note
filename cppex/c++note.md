#1.Intro
##代码、编译和程序
###编译 
```bash
g++ -o  <程序名> <源文件名> 
```
翻译成计算机看得懂的可执行程序

###运行
```bash
./<程序名字>
```
separate the source code into multiple files
eg.
同一个文件夹下
main.cpp   mul.hpp(用于存放函数声明)  mul.cpp(用于写函数体)
其中main.cpp中\#include "mul.hpp"即可
分开编译compile
```bash
g++ -c main.cpp   g++ -c mul.cpp
```
###链接Link
```bash
g++ main.o mul.o -o mul
```
或者
```bash
g++ main.cpp mul.cpp -o mul
```

###Debug
编译错误Compilation errors	eg. 漏;
链接错误Link erros		eg. 在main文件的函数未在头文件声明
运行错误Runtime errors		eg.0作除数

###预处理preprocessor和宏Macros
```cpp
#include <iostream>
#define PI 3.14  //PI替换为3.14
#if defined(_OPENMP)
#include<omp.h>
#endif
```
预处理器将#后内容预处理后送给编译器编译

###simple input and output
c++ style output and input
what is cout?
```cpp
std::ostream cout;
```
cout is an object of data type ostream in namespace std
cout是一个对象
```cpp
cout<<"Hello"<<endl;
```
endl换行符号
c++的输入输出采用流的概念
```cpp
float a;
int b;
cin>>a;
cin>>b;
```
```cpp
//命令行参数查看器

# ===argument.cpp===
#include<iostream>
using namespace std;
int main(int argc, char ** argv)
{
	for(int i=0;i<argc;i++)
		cout<<i<<": "<<argv[i]<<endl;
}
```
argc		argument count参数个数
char ** argv	argument vector参数向量 是一个指针数组
```cpp
# ===ex1===
#include <iostream>
using namespace std;
int main(){
        int n;
        cin>>n;
        for(int i=0;i<10;i++)
                cout<<n<<" ";
        cout<<endl;

}

```
#2.Data Types

Integer numbers
```cpp
int i;
int j=10;
```
should be initialized!
```cpp
int a=56789;
int b=56789;
int c=a*b;
cout<<c<<endl;
```
数值溢出output is negative
unsigned int 无符号 表示正数
signed int[-2^31^,2^31^-1]
unsigned int[2^32^]
还有short;long;long long

sizeof()  返回占用的字节数

char:type for character, 8-bit integer indeed
signed char  unsigned char
```cpp
char c1='C';	//C
char c2=80;	//P
char c3=0x50	//P
```
根据编码转换为字符


表示汉字
```
char16_t c=u'于';
char32_t c=U'于';
```
bool 1byte8bits
true(1/非零)false(0)
```cpp
ex2
//bool变量 true false 非0true 0false
#include<iostream>
using namespace std;
int main(){
        bool flag=true;
        bool flag2=-1;
        bool flag3=0;
        cout<<flag<<" "<<flag2<<" "<<flag3<<endl;
        return 0;

}
//output 1 1 0
```
size_t:
unsigned integer 专门用来数数的无符号整数类型
type of the result of sizeof operator
表示内存大小
```cpp
int arr[100];
size_t size=sizeof(arr);
```
表示容器内有多少个元素
```
vector<int> v={1,2,3,4,5,6};
size_t count=v.size();
```
作为数组容器的索引
```cpp
for(size_t i=0;i<v.size();i++)
{	cout<<b[i];
}
```

floating point numbers
十进制的小数无法被二进制准确表示 会存在精度误差
float i=1.2f;
float=sign+exponent+fraction 
一般用fabs(f1-f2)<FLT_EPSILON来比较两个浮点数是否相等（差的绝对值在误差范围内）
inf:infinity
nan:not a number

Arithmetic Operators
95//decimal十进制		95//int
0137//octal八进制		95u//unsigned int
0x5F//hexadecimal十六进制	95l//long
				95ul//unsigned long
3.14159
6.02e23//6.02*10^23	1.6e-19//1.6*10^-19
6.02e23L//long double
6.02e23f//float
6.02e23//double

const type qualifier
const float PI = 3.1415926f;
PI+=1;//error!
比C的const更严格 可用来表达数组长度 不可以通过指针改变大小 必须被初始化
```cpp
ex3
#include<iostream>
using namespace std;
int main(){
	const int MAX=150;
//相当于#define MAZ 150
//C的const可用指针改变
	cout<<MAX<<endl;
	return 0;

}
```

auto 
auto 会根据初始化定义变量的类型C++中使用必须初始化

question:
auto a=2;
a=3.3;
output a?//输出为3 因为a已经被定义为了int 变量类型不改变

Arithmetic operators
+ - * / ^ % 
bitwise NOT	~a
bitwise AND	a & b
bitwise OR	a | b
bitwise XOR	a ^ b
bitwise left shift	a << b
bitwise right shift	a >> b
优先级
a++ ++a */ +- <<>>

implicit conversion隐式转换
explicit conversion显式转换
char short int long float double long double

Divisions
float f=17/5;//3
精度低的变量和精度高的变量进行运算 结果会是精度高的那种类型


#3.控制流语句 和 循环
```cpp
if statement
if (condition)
{
	语句
}
```
单行语句可不加花括号

```cpp
if (condition1)
{}
else if (condition2)
{}
else
{}
```
bool isPositive=true;
int factor=0;
factor=isPositive?1:-1;
或者写成factor=(isPositive)*2-1
(条件)?(true时返回的值):(false时返回的值)
Conditons
the condition shuold be an expression which is convertible to bool
relational expressions
== != <= >= < <
return 1 if condition is true
return 0 if false

logical expressions 连接两个布尔表达式最终输出一个布尔值
!	not
&&	and
||	or
优先级从上到下
(-2 && true)=true
会转换成布尔类型 -2 ->true
数据可转换成布尔类型implicitly

pointers are also frequently used as conditions
int *p=new int[1024];
if (!p)//if p==NULL
	cout<<"Memory allocation failed"<<endl;

while loop
```cpp
while(){}

do
{
}while();
```
break跳出循环
continue 跳出本次循环 进入下次循环
```cpp
for loop
for (init-clause;cond-expression;iteration-expression)
{}
```

while(num>0) -> for(;num>0;)

for(;;)->while(true)

goto跳转

```cpp
eg.希望算出0-1的浮点数的平方
float mysquare(float value)
{
	float result=0.0f;
	if(value>=1.0f || value<=0)
	{
	cerr<<"The input is out of range."<<endl;
	goto EXIT_ERROR;
	}
	result=value * value;
	return result;
	
	EXIT_ERROR:
	//do sth such as closing files here
	return 0.0f;
}
```
switch语句
```cpp
switch (input_char)
{
	case 'a':
	case 'A':
		cout<<"Move left"<<endl;
		break;
	case 'd':
	case 'D':
		cout<<"Move right"<<endl;
		break;
	default:
		cout<<"Undefined key."<<end;;
		break;		
}
	//DON'T forget break!
```

#4.
##Arrays数组
```cpp
int num_array1[5];
int num_array2[5]={0,1,2,3,4}; //initialization
int num_array[]={1,2,3,4}
```
传入函数时数组会退化为指针,还要传入数组长度
float array_sum(float values[],size_t length);
float array_sum(float *values,size_t length);
数组名字是数组的首地址
不可array1=array2;

###multidimensional arrays
```cpp
int mat[2][3]={{11,12,13},{14,15,16}};
for(int r=0;r<rows;r++)
{	
	for(int c=0;c<cols;c++)
		cout<<mat[r][c]<<",";
	cout<<endl;
}
```

```cpp
void init_2d_array(float mat[][3],size_t rows,size_t cols)
//一定要传列数
```

###const Arrays
```cpp
const float values[4]={1.1f,2.2f,3.3f,4.4f};
```
used as function arguments
数组无法被改变 更安全

```cpp
float array_sum(const float values[],size_t length)
{
	float sum=0.0f;
	for(int i=0;i<length;i++)
	{
		sum+=values[i];
		//values[i]=0;
	}
	return sum;
}
//调用函数
float sum=array_sum(values,4);
```
##Strings
Array-style strings
```cpp
char rabbit[16]={'P','e','t','e','r'};
char bad_pig[9]={'P','e','t','e','r',' ','P','i','g'}
//会报错 需要有位置放字符串结束符\0(默认存在)
char good_pig[10]={'P','e','t','e','r',' ','P','i','g','\0'}
cout << good_pig; 
//会一直输出 直到遇到内存中的\0 \0也占一个字节
cout<<strlen(rabbit)<<endl;
size_t strlen(const char *str);
```

string literals
```cpp
char name1[]="SUSTech";
char name2[]="SUST" "ech";
cout<<name1<<endl;
//SUSTech
cout<<name2<<endl;
//SUSTech
//不加中括号也合法
```

字符串的操作String manipulation and examination

copy
```cpp
strncpy(char *dest,const char *src,size_t count);
//拷贝到\0结束
```

append
```cpp
strcat(char *dest,const char *src);
```
compare
```cpp
strcmp(const char *lhs,const char *rhs)
//比较两个字符串是否相等 相等返回0
//按字典序排
//<返回负数
```


###string class
```
using namespace std;
string str1="Hello";
string str2="SUSTech";
string result=str1+","+"str2";
cout<<"result"+result<<endl;
cout<<"The length is "<<result.length()<<endl;
cout<<"str1<str2 is "<<(str1<str1)<<endl;
```
```cpp
ex4
#include <iostream>
using namespace std;
int main()
{
        string s ="hello";
        string s2="world";
        string s3=s+s2;
        string s4;
        getline(cin,s4);//获取一行
        cout<<s3<<endl;
        cout<<s4<<endl;
        cout<<s.length()<<endl;
        cout<<s4.length()<<endl;
        string s_sub=s.substr(1,2);
        cout << s_sub<<endl;
        //substr(1,2)从第[1]个字符开始数 输出两个字符组成的子字符串
        //[0]才是第一个字符
        return 0;
}

//cin只能获取单个单词 换行回车都视为结束
//s.length()计算长度 是字符串的方法
//空格长度为1
```

##Structure Unions Enumerations
a struct is a type consisting of a sequence of members
```cpp
struct Student{
	char name[4];
	int born;
	bool male;
};
struct Student stu1;
strcpy(stu1.name,"Yu");
stu1.born=2000;
stu.male=true
```
通过  . 访问结构体成员
也可以这样初始化
```cpp
struct Student stu={"Yu",2000,true};
Student stu={.name="Yu", .born=2000, .male=true};
```


c++可去除struct
c中可通过typedef来操作
```c
typedef
struct _Student{
	char name[4];
	int born;
	bool male;
}Student;
```

结构体数组
```cpp
struct Student students[100];
sutdents[20].born=2002;
```

内存
name		born	   male	
 0   1   2  3  4  5  6  7  8     9  10  11  12  13
'Y' 'U'  0  0  2  0  0  0  1 
```cpp
struct Student1{
	int id;
	bool male;
	char label;
	float height;
};
struct Student2{
	int id;
	bool male;
	float height;
	char label;
};
sizeof(Student1)//12
sizeof(Student2)//16
//一个寄存器是八个字节 数据不跨寄存器存储为了传输更加高效 所以部分字节会闲置
//struct 和 class在C++中十分类似 typedef 在C++中并不常用
```
Union联合体
```cpp
union ipv4address{
	std::uint32_t address32;//uin32_t 4个字节
	std::uint8_t address8[4];//uint8_t 1个字节
};
int main()
{	
	union ipv4address ip;
	cout<<sizeof(ip)<<endl //4
	ip.address8[3]=127;
	ip.address8[2]=0;
	ip.address8[1]=0;
	ip.address8[0]=1;
	
	cout<<std::hex;//让cout以十六进制的格式输出整数  x=255; cout<<hex<<x<<endl;输出ff hex具有粘性 后面在cout输出的都是十六进制
	cout<<"in hex"<<ip.address32<<endl;

	return 0;
}
```
Enum
```cpp
enum color{WHITE,BLACK,RED,GREEN,BLUE,YELLOW,NUM_COLORS};//0123456
enum color{WhITE=1,BLACK=2,RED,GREEN}//自动填充
```

```cpp
eg.
enum datatype{TYPE_INT8=1,TYPE_INT16=2,TYPE_INT32=4,TYPEINT64=8};
struct Point{//表示三维世界的一个点
	enum datatype type;
	union{
		std::int8_t data7[3];
		std::int16_t data16[3];
		std::int32_t data32[3];
		std::int64_t data64[3];
	};
};
size_t datawidth(struct Point pt)
{
	return size_t(pt.type)*3;
}
int 64_t l1norm(struct Point pt)
{
	int64_t result=0;
	switch(pt.type)
	{
		case(TYPE_INT8):
			result=abs(pt.data8[0])+abs(pt.data[1])+abs(pt.data[2]);
			...

//l1范数|x|+|y|+|z|
```
###typedef
can be used to replace a possibly complex type name
```cpp
eg.
typedef int myint;
myint num=32;

typedef struct _rgb_struct{
	unsigned char r;
	unsigned char g;
	unsigned char b;
}rgb_struct;
//定义结构体的同时顺便起了一个别名
rgb_struct rgb={0,255,128};
```

```cpp
ex5
#include<iostream>
using namespace std;
struct stu{
	string name;
	int age;
};
int main(){
	stu a[10];
//不需要加 struct stu a[10];
//也不用typedef
	return 0;
}
```

#5.Pointers
what stored in a pointer variable is an address
operator & can take the address of an object or a variable of fundamental types
operator * can take the content that the pointer points to 解引用
#整型指针
```cpp
eg.
int num=10;		
```
0x03
0x02
0x01
0x00
假设这四个字节存储num
```cpp
int *p1=&num;
int *p2=&num;都指向0x00
*p1=20; 直接修改了num
```

##结构体指针
```cpp
struct Student{};
Student *p;
结构体指针
访问结构体p的成员
p->member
(*p).member
//两种形式等价
```

```
eg.
struct Student
{
	char name[4];
	int born;
	bool male;
};
Student stu={"Yu",2000,true};
Student *pStu=&stu;指向结构体的首地址
strncpy(pStu->name,"Li",4);
pStu->born=2001;
(*pStu).born=2002;
pStu->male=false;
cout<<"Address of stu: "<<pStu<<endl;
cout<<"Address of member name: "<<&(pStu->name)<<endl;
cout<<"size of (pStu) is "<<sizeof(pStu)<<endl;//x64 8
```
##Pointers of pointers
```cpp
int num=10;
int *p=&num;
int **pp=&p;
*(*pp)=20;  //num=20
```

```cpp
int num=1;
int another=2;
//You cannot change the value that p1 points to through p1
const int *p1=&num;
*p1=3 //error
num=3;//okay
//You cannot change value of p2(address)
int * const p2=&num;
*p2=3;//okay
p2=&another;//error
```
const int* const p3=&num;
cannot change either of them

int foo(const char *p) //防止指针被修改
{
//the value that p points to cannot be changed
char *p2=p;//syntax error 类型不同const char *p2=p; 用p2只读访问数据
return 0;
}

Pointers and arrays
Student students[128] 结构体数组
Student * p0=&students[0];
Student * p1=&students[1];
第[0],[1]个结构体的首地址
students[1].born=2000;
p1->born=2000;
解引用蕴含在表达式当中
&students 
students 
&students[0]
都是数组的首地址

Pointer arithmetic
p+num  points to the num-th element of the array p
p-num points to the -num-th element
会根据指针的类型偏移相应的字节数
int numbers[4]={0,1,2,3};
int *p=numbers+1; //指向1
p++;

*p=20;				3	30
*(p-1)=10;		   p->	2	20
p[1]=30;  p当数组用		1	10
				0

宏
#define PRINT_ARRAY(array,n)\ \
for (int idx=0;idx<(n);idx++)\
	cout<<"array["<<idx<<"]="<<(array)[idx]<<endl;
//转义 使宏可以写成多行

Array is a constant pointer
the total size of all elements in an array can be got by sizeof
but sizeof operator to a pointer will return the size of the address(4 or 8)
会返回地址所占用的字节数
Allocate memory
栈（默认内存）通常较小
堆（申请的内存）取决于电脑的剩余内存
如果程序需要处理一张数据量很大的图片 一个3D模型等 
放到栈上 可能导致栈溢出 程序崩溃
所以要申请放到堆里
或者
内存需要活到函数结束之后
栈上的变量：函数执行完后自动销毁
堆上的变量：不delete就永远存在
eg.在游戏里创建了一个Player 对象 玩家要活着直到被杀死或者游戏结束
struct Player{};
Player* createPlayer()
{	
	Player p;
	return &p;
}
他必须跨函数存活 故必须申请放到堆里

C style
指针指向的内存是动态申请的
程序运行时 操作系统会给程序的运行分配一段空间
__________________
	stack		栈 local variables, call stack		函数调用的现场
------------------
	  ⬇
	  

	  ^
	  |	
------------------	
	heap		堆 dynamically allocated memory		new 或 malloc分配的内存
------------------
uninitialized data
	bss
__________________	未初始化的静态数据 包括变量和常量	static int x;或者int y;(全局) 
initialized data
	data		初始化静态变量	eg.static int x=10;
__________________
executable code		可运行代码	程序编译后的二进制指令，只读
      code/text

程序从堆申请地址 栈越申请越小 堆的地址越申请越大

Allocate size bytes of uninitialized storage
malloc函数原型void* malloc(size_t size) 字节数
int * p1=(int*)malloc(4);
强制转换为整型指针

释放内存
The dynamically allocated memory must be deallocated explicitly
void free(void* ptr)
p=(int*)malloc(4*sizeof(int));//内存被浪费了
//...
p=(int*)malloc(8*sizeof(int));
//...
free(p)

void foo()
{	
	int* p=(int*)malloc(sizeof(int));
	return;
}//memory leak内存申请后未释放 导致内存浪费
有申请 有释放！


CPP style
申请内存new new[]
Operator new is similar with malloc() but with more features 
int *p1=new int;//输出操作完后内存的地址
//allocate an int, default initializer(do nothing)
int *p2=new int();	可把括号改为花括号
//allocate an int, initialized to 0;
int *p3=new int(5)	可把括号改为花括号
//allocate an int, initialize to 5;

Student * ps1=new Student;			//allocate a Student object, default initializer
Student * ps2=new Student {"Yu",2020,1};	//allocate a Student object, initialize the members

int * pa1=new int[16];//allocate 16 int 未初始化
int * pa2=new int[16];//allocate 16 int, zero initialized
int * pa4=new int[16]{1,2,3}; //first 3 elements are initialized to 1,2,3, the rest 0

Student * psa1=new Student[16];//allocate memory for 16 Student objects, default initializer
Student * psa2=new Student[16]{{"Li",2000,1},{"Yu",2000,0}};//初始化前两个其他置0
//new的返回值是一个指针 所以要用指针接着
int* p=new int{10} 分配一块内存初始化为10
//圆括号花括号均可
int* arr=new int[10];
//分配十个int 未初始化
int* arr=new int[5]{1,2,3,4,5};
//分配五个int并且初始化
{}  ()表示初始化为0 初始化数字不足的补0



释放内存
delete delete[]
delete p1;
delete ps1;//deallocate memory
delete pa1;
delete []pa2;//deallocate the memory of the array

delete psa1;//deallocate the memory of the array, and call the destructor of the first element 释放全部内存但只调用第一个元素的析构函数 造成内存泄漏
delete []psa2;//deallocate the memory of the array, and calll the destructors of all elements	调用每个元素的析构函数 释放整块内存 安全
涉及到类 结构体 数组最好加[]


6.Functions
#include <iostream>
#include <cfloat>
using namespace std;

struct Matrix {
    int rows;
    int cols;
    float* pData;
};

// 封装的函数：找矩阵最大值
float findMaxValue(const Matrix& mat) {
    float maxa = FLT_MIN;				//float类型的最小值
    for (int r = 0; r < mat.rows; r++) {
        for (int c = 0; c < mat.cols; c++) {
            float val = mat.pData[r * mat.cols + c];	//指针可通过类似数组下标的方式访问
            if (val > maxa) {
                maxa = val;
            }
        }
    }
    return maxa;
}

int main() {
    // 创建矩阵
    Matrix matA;
    matA.rows = 2;
    matA.cols = 3;
    matA.pData = new float[matA.rows * matA.cols];
    //new返回这块内存的首地址
    // 填充数据
    float data[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    for (int i = 0; i < matA.rows * matA.cols; i++) {
        matA.pData[i] = data[i];
    }
    //复制data到matA
    // 使用封装的函数
    float maxVal = findMaxValue(matA);
    cout << "最大值: " << maxVal << endl;  // 6
    
    delete[] matA.pData;
    return 0;
}

还可以这样初始化
Matrix matA={3,4};//三行四列
matA.pData=new float[matA.rows*matA.cols]{1.f,2.f,3.f};//其他元素自动赋0

eg.
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


函数声明
返回类型 函数名 (参数类型 参数列表);

draw.h
//用于写函数原型
#ifndef __DRAW_H__
#define __DRAW_H__
//相当于给这个文件下一个标记 让最后的程序只出现一次这个标记
//防止一个头文件被重复include 从而报错
bool drawLine(int x1,int y1,int x2,int y2);
bool drawRectangle(int x1,int y1,int x2,int y2);
#endif

draw.cpp
//用于写函数体

main.cpp


How are functions called?
二进制指令一条条往里面搬运
函数调用会导致跳转
当前状态会被保存（压栈）
function执行完后
状态从栈中取出
The cost to call a function!

function parameters
1.pass by value		传值调用
2.pass by reference	

pass by value
将数据复制后传入函数 但函数调用不改变原数据
int foo(int *p)
{
	(*p)+=10;
	return *p
}

int num1=20;
int *p=&num1;
num2=foo(p);
传进去的是p地址的复制值
会改变num1的值 但是不改变p的值 依然是传值的逻辑

If the structure is a huge one, such as 1K bytes
A copy will cost 1kb memory and time consuming to copy it.
So we can pass the pointer that stores the address of the structure or use reference

pass by reference 引用(C++)
a reference is an alias to an already-existing variable/object
别名
int num=0;
int & num_ref=num;给num起了一个别名
//&写在类型后面是引用 写在变量前面是取地址
num_ref=10
//num=10也会发生变化
//引用必须初始化
References are much safer
const struct Matrix & mat提供只读保护


使用Valgrind
Valgrind是一个内存测试、内存泄漏检测和性能分析工具



ex6
//引用和传址
#include<iostream>
using namespace std;
void c(int &a)
{a+=1;
}
//定义了一个函数
//c++的引用和c的取地址符号没有关系
int main(){
int a=4;
c(a);
cout<<a<<endl;
return 0;
}
//这里&是引用会改变函数值，如果去掉则不会改变



Return statement
return;只适用于void类型函数
return 语句会把其后的值自动转换成函数返回类型再返回 隐式类型转换

指针函数返回指针
Matrix* create_matrix(int rows,int cols)
{
//检查输入是否合法
	Matrix *p=new Matrix{rows,cols};		//用于存放结构体的成员
	p->pData=new float[p->rows*p->cols];		//用于存放矩阵数据
	//you should check if the memory is allocated successfully
	//don't forget to release the memory
	return p;
}


结构体函数返回的是整个结构体
eg.
Matrix createMatrix(int rows,int cols)
{
	Matrix mat;
	mat.rows=rows;
	mat.cols=cols;
	mat.pData=new float[rows*cols];
	return mat;
}

int main()
{
	Matrix m=createMatrix(3,4);
	return 0;
	delete[] m.pData
}

函数调用暗含赋值操作 引用的等号更像是绑定 比普通的赋值更紧密

If we have a lot to return
such as a matrix addition function(A+B->C)
Suggested
use reference to avoid data copying
use const parameters to avoid the input data is modified
use non-const reference parameters to receive the output

bool matrix_add(const Matrix & matA,const Matrix & matB,Matrix &matC)
{
	//check the dimensions of the three matrices
	//re-create matC if needed 重新释放 申请
	//do matC=matA+matB
	//return true if everying is right
}



Inline function
Stack operations and jumps are needed for a function call
It is a heavy cost for some frequently called tiny functions
//为避免频繁的压栈 出栈 针对频繁调用的小函数可以将其写成inline function
eg.
float max_function(float a,float b)
{
	if (a>b)
		return a;
	else
		return b;
}
//可以用?:替换
	int num1=20;
	int num2=30;
	int maxv=max_function(num1,num2);
}

inline float max_function(float a,float b)
{...}

高地址
+=============================================+
|                 内核空间                      |  ← 操作系统内核代码和数据
|          （用户态不可访问）                   |
+---------------------------------------------+
|                                              |
|             栈（Stack）                       |  ← 局部变量、函数参数、返回地址
|             ⬇ 向下增长                      |
|                                              |
+---------------------------------------------+
|                 空洞区域                      |  ← 栈和堆之间的未映射区域
|                                              |
+---------------------------------------------+
|                                              |
|             堆（Heap）                       |  ← new / malloc 动态分配的内存
|             ⬆ 向上增长                      |
|                                              |
+---------------------------------------------+
|        未初始化数据段（.bss）                |  ← 未初始化的全局变量、静态变量
|                                              |     程序启动时由系统清零
+---------------------------------------------+
|        已初始化数据段（.data）               |  ← 已初始化的全局变量、静态变量
|                                              |     可读可写
+---------------------------------------------+
|             只读数据段（.rodata）             |  ← 字符串常量、const 修饰的全局变量
|                                              |     只读，不能修改
+---------------------------------------------+
|             代码段（.text）                  |  ← 编译后的机器指令
|             只读，不可修改                    |     main 函数、普通函数、未展开的 inline 函数
+---------------------------------------------+
低地址                                        （传统情况下，代码段位于低地址）
会和main一起进入指令流

inline只是建议编译器这样操作

why not use a macros?
#define MAX_MACRO(a,b) (a)>(b)?(a):(b)
宏是整体替换
maxv=MAX_MACRO(num1++,num2++)
最大值将会是加一后的其中一个值
和函数的结果不同
不加圆括号可能出错








lambda
// Python 写法
add = lambda x, y: x + y

// C++ 写法（几乎一样）
auto add = [](int x, int y) { return x + y; };

// C++甚至可以捕获外部变量
int result = add(10, 20);  // 30
int factor = 2;
auto multiply = [factor](int x) { return x * factor; };  // 捕获 factor
cout << multiply(5) << endl;  // 10

语法
[捕获列表](参数列表)->返回类型{函数体}
返回类型可以让编译器自己猜
auto sayHello=[](){cout<<"Hello";};
sayHello();

auto add=[](int a,int b)->int{return a+b;};
int result=add(3,5);





7.
Default arguments(C++)
默认参数
To call a function without providing one or more trailing arguments
不传这个参数 函数就采用默认参数开始工作
float norm(float x, float y, float z=0);
默认参数只能放到尾部

Overloading(C++)函数重载
C99
<math.h>
double	round(double x)
float	roundf(float x)
C++11
<cmath>
double	round(double x);
float	round(float x);
long double	round(long double x);

Function overloading
多个函数使用同一个名字 但参数不同 类型、个数可以不同
参数名要相同 默认参数不可冲突
void foo(int a);
void foo(int a,int b);

choose the function according to the argument 
Argument-dependent lookup ADL
eg.
int sum(int x,int y)
{
	cout<<"sum(int,int) is called"<<endl;
	return x+y;
}

float sum(float x,float y)
{
	cout<<"sum(float,float) is called"<<endl;
	return x+y;
}

double sum(double x,double y);
不能重定义 需要参数类型不同 参数名相同
仅返回值不同 不可重载

Function templates
函数模板
函数重载下 函数的修改变得比较机械重复
有没有什么东西可以生成多个相似的函数呢？？

Explicit Instantiation
显式实例化
A function template is not a type, or a function, or any other entity
No code is generated from a source file that contains only template definitions
The template arguments must be determined, then the compiler can generate an actual function
只有确定了模板参数（T的具体类型）后 编译器才能生成一个真正的参数
sum<int> or sum<double>


template<typename T>
T sum(T x,T y)
{
	cout<<"The input type is "<<typeid(T).name() <<endl;
	return x+y;
}
其实就是把T全部替换掉
//instantiates sum<double>(double,double)
template double sum<double>(double,double);

template char sum<>(char,char);

template int sum(int,int);

只是提前生成一个版本 不会影响别的版本的生成

隐式实例化
cout<<"sum= "<<sum<float>(2.2f,3.0f)<<endl;
<float>也可省去



如果T是结构体 该怎么办？
结构体没有加法 
Specialization for Point + Point operation

struct Point
{
	int x;
	int y;
};
template<typename T> 
T sum(T x,T y);
特例化 要加尖括号 否则会被视为实例化
template<>
Point sum<Point>(Point pt1,Point pt2)
{
	Point pt;
	pt.x=pt1.x+pt2.x;
	pt.y=pt1.y+pt2.y;
	return pt;
}


eg.
#include<iostream>
using namespace std;
template<typename T>
T sum(T x,T y)
{
        cout<<"The input type is "<<typeid(T).name()<<endl;
        return x+y;
}
struct Point
{
        int x;
        int y;
};
template<>
Point sum<Point>(Point pt1,Point pt2)		明确指定T为point
{
        cout<<"The input type is "<<typeid(pt1).name()<<endl;
        Point pt;
        pt.x=pt1.x+pt2.x;
        pt.y=pt1.y+pt2.y;
        return pt;
}
int main()
{
        cout<<sum(1,2)<<endl;
        Point p1={1,5};
        Point p2={2,4};
        Point pt=sum(p1,p2);
        cout<<"pt=("<<pt.x<<","<<pt.y<<")"<<endl;
        return 0;
}

//特例化结构必须一致


Function pointers
函数指针
eg.
float norm_l1(float x,float y);
float norm_l2(float x,float y);
float (*norm_ptr)(float x,float y);
要完全匹配
norm_ptr=norm_l1;//pointing norm_l1
norm_ptr=&norm_l2;//Pointing norm_l2
两种指向方式等价

float len1=norm_ptr(-3.0f,4.0f);
float len2=(*norm_ptr)(-3.0f,4.0f);
两种调用方式

A function pointer can be an argument and pass to a function
用于灵活调用函数
<stdlib.h>
void qsort(void *ptr,size_t count,size_t size, int(*comp)(const void *,const void *));
To struct some customized types, such as
struct Point
struct Persion
*comp就是比较的依据 使用指针调用函数作为排序的依据

Function references
函数引用
float norm_l1(float x,float y);
float norm_l2(float x,float y);
float (&norm_ref)(float x,float y)=norm_l1;
函数别名

函数名其实也是一个指针
&function和function值相同 类型相同




Recursive Function
递归函数
void div2(double val)
{
	cout<<"Entering val= "<<val<<endl;
	if(val>1.0)
		div(val/2);//function call itself
	else
		cout<<"-----------------"<<endl;
	cout<<"Leaving val="<<val<<endl;
}
如果条件改为val>-1.0 回报错
Pros:
Good at tree traversal
Less lines of source code

Cons:
Consume more stack memory
Maybe slow
Difficult to implement and debug

函数递归是一个栈结构 先进后出




#8.
##C/C++ with ARM
Intel VS ARM
了解硬件 才能写出好的代码
Intel占领服务器和个人电脑市场，但是功耗很大 近年来市场份额下降 
大部分手机电视无人机使用ARM CPU 个人电脑使用ARM CPU
ARM CPU功耗低

使用ARM服务器提升代码效率

Raspberry Pi 4树莓派
相当于小型个人电脑
上面是Linux操作系统

How to develop programs with ARM
Development boards
Almost the same with x86 PC with Linux OS
-g++ 
-Makefile
-cmake

##speedup your program
**Simple is Beautiful**
*Short* *Simple* *Efficient*


Some Tips On Optimization
-Choose an appropriate algorithm 时间复杂度 空间复杂度
-Clear and simple code for the compiler to optimize 机器可读性
-Optimize code for memory 优化内存读写 连续读写内存
-Do not copy large memory 避免内存拷贝
-No printf()/cout in loops 
-Table lookup(sin(),cos()...) 查表法（对精度要求不高）提前设置一个数组 存放三角函数值 用内存换时间
-SIMD,OpenMP ?


Example
Face detection and facial landmark detection in 1600 lines of source code
//采用卷积神经网络CNN
https://github.com/ShiqiYu/libfacedetection

###SIMD:single instruction, multiple data
eg.
(x,y,z,w)四维向量加法 操作方式一般是四个分量两两相加
Scalar Operation of Vector Length 4
SIMD可以只做一次加法 
指令
-Intel:MMX,SSE,SSE2,AVX,AVX2,AVX512 
-ARM:NEON
-RISC-V:RVV(RISC-V Vector Extension)
可以实现

SIMD in OpenCV
"Universal intrinsics" is a types and function set intended to simplify vectorization of code on different platforms
使用OpenCV中的universal intrinsics为算法提速

SIMD只使用了一个CPU内核
###OpenMP
可以将任务分给各个CPU运行
拆任务需要时间
```cpp
#include <omp.h>
#pragma omp parallel for
for(size_t i=0;i<n;i++)
{
	//#pragma omp parallel for
	for(size_t j=0;j<n;j++)
	{
		//...
	}
}
```
循环体相互依赖无法并行运行

###An example with SIMD and OpenMP
在华为云服务器上运行函数
ARM Cloud Server
Huawei ARM Cloud Server
Kunpeng 920(2 cores)
RAM: 3GB
openEuler Linux

Functions for dot product
```cpp
float dotproduct(const float *p1,const float *p2,size_t n);
float dotproduct_unloop(const float *p1,const float *p2,size_t n);	//循环展开
float dotproduct_avx2(const float *p1,const float *p2,size_t n);	//借助SIMD和OpenMP实现
float dotproduct_avx2_omp(const float *p1,const float *p2,size_t n);
float dotproduct_neon(const float *p1,const float *p2,size_t n);
float dotproduct_neon_omp(const float *p1,const float *p2,size_t n);
```

```cpp
float dotproduct(const float *p1,const float *p2,size_t n)
{
	float sum=0.0f;
	for(size_t i=0;i<n;i++)
		sum+=(p1[i]*p2[2]);
	return sum;
}
//判断i<n有代价
```

```cpp
float dotproduct_unloop(const float *p1,const float *p2,size_t n)
{
	if(n%8!=0)
	{
		std::cerr<<"The size n must be a miltiple of 8."<<std::endl;
		return 0.0f
	}
	float sum=0.0f;
	for(size_t i=0;i<n;i+=8)
	{
		sum+=(p1[i]*p2[i]);
		sum+=(p1[i+1]*p2[i+1]);
		sum+=(p1[i+2]*p2[i+2]);
		sum+=(p1[i+3]*p2[i+3]);
		sum+=(p1[i+4]*p2[i+4]);
		sum+=(p1[i+5]*p2[i+5]);
		sum+=(p1[i+6]*p2[i+6]);
		sum+=(p1[i+7]*p2[i+7]);
	}
	return sum;
//减少循环次数
}
```


```cpp
#pragma once

//确保头文件只被包含一次
//pragma用于控制编译器的行为
```


###Avoid Memory Copy in OpenCV
What's an image?
黑白照片0-255   0为纯黑 255为纯白
彩色图片R(0-255) G(0-255) B(0-255)
数值代表亮度 强度
```cpp
cv::Mat class
class CV_EXPORTS Mat
{
public:
	//some members
	int rows,cols;
	//pointer to data
	uchar* data;
	//size_t step.p
	MatStep step;
};
```

可能有很多指针都指向一个Matrix的头 那么谁来释放内存？
int* refcount引用计数 记录某块内存被多少个头指向 值变为0则可以销毁这块内存
step表示每一行元素有多少个字节
How many bytes for a row of Matrix 4*3
Can be a value>=3
Memory alignment for SIMD

ROI: Region of interest
在不复制像素数据的情况下 高效地操作图像中的一小块区域
Mat A
rows=100
cols=100
data=0xABCDEF00

Mat B
rows=100
cols=100
step=100
data=0xABCDEF00
//避免了内存的拷贝

//但有时需要指向内存的中间区域
Mat C
rows=30
cols=28
step=100  //下一行的起始地址
data=0xABCE0698
实际上内存是线性的一维的

假设Mat是一张人脸 我们只关心其中鼻子的部分 其中0xABCE0698是这个部分的起始地址 不需要把这块区域copy出来 只需要在原图上操作即可 step=100即可以一行直接到达下一行

#9.类
##classes and objects
A struct in C is a type consisting of a sequence of data members
Some functions/statements are needed to operate the data menbers of an object of a struct type
操作结构体的数据危险且容易出错
类！是更好的选择
###Classes
类不仅有成员数据还有成员函数（方法）
```cpp
class Student
{
	public:
		char name[4];
		int born;
		bool male;
		void setName(const char * s)
		{
			strncpy(name, s, sizeof(name));
		}
		void setBorn(int b)
		{ 
			born=b;
		}
		void setGender(bool isMale)
		{
			male=isMale;
		}
		void printInfo()
		{
			std::cout<<"Name: "<<name<<std::endl;
			std::cout<<"Born in "<<born<<std::endl;
			std::cout<<"Gender: "<<(male ? "Male":"Female")<<std::endl;
		}
};
int main{
	Student yu;
	yu.setName("Yu");
	yu.setBorn(2000);
	yu.setGender(true);
	yu.born=2001;//It can also be manipulated directly
	yu.printInfo()
	std::cout<<"It's name is"<<yu.name<<std::endl;

	return 0;	
}
```
可以直接操作是因为数据设置为了public
//public是cpp的访问控制关键字 决定了谁能访问类中的成员（变量 函数）类外部也可以访问
//protected 只有类内部和派生类（子类）可以访问
//private只有类内部可以访问
```cpp
class Student
{
        private:
		char name[4];
		int born;
		bool male;
	public:
		void setName(const char * s)
                {
                        strncpy(name, s, sizeof(name));
                }
                void setBorn(int b)
                { ...
//Private只能被类内部的成员函数访问
//不写就是默认private
```

```cpp
//在类内部成员函数可以只声明
void setGender(bool isMale);
void printInfo();
//在类外部
inline void Student::setGender(bool isMale)
{
	male=isMale;
}
void Student::printInfo
{
	cout<<"Name: "<<name<<endl;
	...
}
//在类内部定义的成员函数 默认为inline function
//简单的函数 放到类内部定义
//复杂的函数 放到类外部定义
```
类的声明可以放到student.hpp
类函数的定义可以放到student.cpp 要#include "student.hpp"

```
使用cmake

cmake_minimum_required(VERSION3.12)

project(persondemo)

ADD_EXECUTABLE(persondemo main.cpp student.cpp)
//建议进到build cmake ..
```
##Constructors and Destructors
构造函数和析构函数
##Constructor
Different from struct in C, a constructor will be invoked when creating an object of a class
-struct in C: allocate memory
-class in C++:alocate memory and invoke constructor
//The compiler will generate one with empty body
The constructor's name is the same with the class and have no return value
```cpp
class Student
{
        private:
		//...
	public:
		Student()
		{
			name[0]=0;
			born=0;
			male=false;
		}
		//重载
		Student(const char* initName,int initBorn,bool isMale)
		{
			setName(const char * s)
			born=initBorn;
			male=isMale;
		}
};
```


The members can also be initialized as follows
构造函数的另一种写法
```cpp
Student(const char * initName):born(0),male(true)
{
	setName(initName);
}

```

```cpp
public:
	Student()
	{
		name[0]=0;
		born=0;
		male=false;
		cout<<"Constructor:Person()"<<endl;
	}
	Student(const char* initName):born(0),male(true)
	{
		setName(initName);
		cout<<"Constructor:Person(const char*)"<<endl;
	}
	Student(const char* initName,int initBorn,bool isMale)
	{
		setName(initName);
		born=initBorn;
		male=isMale;
		cout<<"Constructor:Person(const char,int,bool)"<<endl;
	}
	

```
运行程序判断哪个构造函数被使用了
Student yu;
//输出为Constructor:Person()
Student Li("Li");
//输出为Constructor:Person(cosnt char*)
Student xue=Student("XueQikun",1962,true);
//输出为Constructor:Person(const char,int,bool)
且打印出问题了因为strncpy只拷贝了四个字符 char name[4]
无终止符导致乱码

##Destructor
销毁一个函数
The destructor will be invoked when object is destryed
Be formed from the class name preceded by a tilde ~
Have no return value, no parameters

```cpp
class Student
{
	//...
	public:
		Student()
		{
			name=new char[1024]{0};
			born=0;
			male=false;
			cout<<"Constructor:Person()"<<endl;
		}
		~Student()
		{
			delete [] name;
		}

};
//申请释放对应内存
```
```cpp
int main()
{
	{
		Student yu;
		yu.printInfo();
	
		yu.setnName("Yu");
		yu.setBorn(2000);
		yu.setGender(true);
		yu.printInfo();
	}
	Student xue=Student("XueQikun",1962,true);
	Student xue=Student("XueQikun",1962,true);
	xue.printInfo();

	Student * zhou=new Student("Zhou",1991,false);
	zhou->printInfo();
	delete zhou;
	return 0;
}
//对象会在作用域结束之后会被销毁
new出来的对象需要手动销毁
```



```cpp
//使用new 给数组分配内存时 需要使用delete[]
Student * class1=new Student[3]
{
	{"Tom",2000,true},
	{"Bon",2001,true},
	{"Amy",2002,false},...
};
class1[1].printInfo();
//delete class1;  只调用第一个对象的析构函数
//or
//delete []class1;//调用每一个对象的析构函数
//应该选择后者
//只释放内存不调用析构函数会导致永远失去对这块内存的控制权
//就好像住酒店 释放内存就是退房，把房卡交给酒店 告诉外界这个房间可以住人
//但是留在酒店的行李永远无法被使用了
//长期下去 会减少内存 减慢运行速度
```

###this pointer
How does a member function know which name?
```cpp
Student yu=Student{"Yu",2000,true};
Student amy=Student{"Amy",2000,true};
yu.setName("yu");;
amy.setName("Amy");
void setName(const char* s)
{
	strncpy(name,s,1024);
}
当两个不同的对象调用同一个成员函数的时候 这个函数怎么直到该修改哪个对象的数据
serName 如何直到这一次要修改的是yu还是amy的数据？
编译器传了一个this 指针！
All methods in a function have a this pointer
It is set to the address of the object that invokes the mothod
void setBorn(int b)
{
	born=b;
}
实际上：
void setBorn(int b)
{
	this->born=b;
}

void setBorn(int born)
{
	this->born=born;
}

Student(const char * name,int born,bool male)
{
	this->name=new char[1024];
	this->setName(name);
	this->born=born;
	this->male=male;
	cout<<"Constructor: Person(const char,int,bool)"<<endl;

}
函数内部可使用当前对象的指针
```

###const and static members
const Variables
```cpp
#define Value 100 (C)
const int value=100;
const int * p_int;
int const * p_int;
//指针指向的内容不能透过指针修改

int * const p
//指针自己存放的地址不能被修改
//const 在*的哪一侧 哪一侧就无法改变

void func(const int *)
//常用于函数 保证传入变量不被修改 更安全

```

const Members
-const member variables behavior similar with normal const variables
-const member functions promise not to modify member variables 
//函数不可修改成员变量
```cpp
class Student
{
	private:
		const int BMI=24;
		//...
	public:
		Student()
		{
			BMI=25;
			//...
		}
		int getBorn() const
		{
			born++;//会报错 无法修改成员变量
			return born;

		}


}
```


###static members
static members are not bound to class instances.
//静态成员不绑定到类的实例 变量只有一份 被所有成员共享
```cpp
class Student
{
	private:
		static size_t student_total;//declaration only只声明
	public:
		Student()
		{
			student_total++;//每创建一个对象 总数加一
		}
		~Student()
		{
			student_total--;
		}
		static size_t getTotal() {return student_total;}
		//静态函数

};
//definition it here
size_t Student::student_total=0;
类外定义 静态成员必须在类外单独定义 分配内存

//可以在Constructor和Destructor中执行一个打印命令观察输出。
int main()
{	
	cout<<"--We have "<<Student::getTotal()<<" students--"<<endl;
}
//静态函数不依赖任何对象 不能操作非静态变量
```

#10.运算符的重载
##operators in opencv
Operators for cv::Mat
//函数有相同的函数名 但是有不同的变量 有函数重载
```cpp
Mat mul(Mat& A,Mat& B);
Mat mul(Mat& A,float b);
Mat mul(float a,Mat& B);
```

```cpp
More convenient to code
Mat A,B;
float a,b;
//...
Mat C=A+B;
Mat D=A*B;
Mat E=a*A;
//操作符重载非常方便
```

eg.
```cpp
#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
int main()
{
	float a[6]={1.0f,1.0f,1.0f,2.0f,2.0f,2.0f};
	float b[6]={1.0f,2.0f,3.0f,4.0f,5.0f,6.0f};
	cv::Mat A(2,3,CV_32FC1,a);//2行3列 32位浮点数 C1单通道矩阵 数据来自a
	cv::Mat B(3,2,CV_32FC1,b);//同理

	cv::Mat C=A*B;//重载

	cout<<"Matrix C= "<<endl
		<<C<<endl;//重载
return 0;
}
}
//output:Matrix C=[9,12
		  18,24]
```
如何实现呢？？
Operator overloading
Customizes the C++ for operands of user-defined types
Overload operators are functions with special function names:
```cpp
#include<string>

std::string s("Hello");
s+="C";//overloading
s.operator+=(" and CPP!")
//最后两行两个操作等价
```
##Operator overloading //Actually a function
-Implementation of operator+() and operator+=() and operator+=()
```cpp
class MyTime
{
	int hours;
	int minutes;
	public:
		MyTime():hours(0),minutes(0){} 
		//构造函数的写法 函数名:初始化列表 函数体
		/*等价于
		MyTime(){
			hours=0;
			minuts=0;
		}
		*/
		MyTime(int h,int m):hours(h),minutes(m){}

		MyTime operator+(const MyTime & t) const
		{
			MyTime sum;
			sum.minutes=this->minutes+t.minutes;
			sum.hours=this->hours+t.hours;
			sum.hours+=sum.minutes/60;
			sum.minutes%=60;
			return sum;
		}//只修改了sum
		std::string getTime() const;
};
//完成了operator+()的重载
```

operator+=的重载
```cpp
MyTime & operator+=(const MyTime & t)//引用传递
{//引用返回
	this->minutes+=t.minutes;
	this->hours+=t.hours;

	this->hours+=this->minutes/60;
	this->minutes%=60;

	return *this;
	
}//修改自身返回自身
```


If one operand is not MyTime, and is an int
What about MyTime t2=t1+20; ?
The function can be
```cpp
MyTime operator+(int m) const
{
	MyTime sum;
	sum.minutes=this->minutes+m;
	sun.hours=this->hours;
	sum.hours+=sum.minutes/60;
	sum.minutes%60;
	return sum;
}
//再重载一次
```

```cpp
MyTime operator+(const std::string str) const
{
	MyTime sum=*this;
	if(str=="one hour")
		sum.hours=this->hours+1;
	else
		std::cerr<<"Only\"one hour\" is supported."<<std::endl;
}
//实现了+"one hour"
```
How about the expression 20+t1; ?

##Friend Function









```cpp
//stl篇stl是Standard Template Library标准模板库 是C++标准库的核心组成部分
//本质上是一套数据结构与算法的工具箱
//vector 动态大小 可以随意增删元素的数组替代品 向量
//在<vector>里面 
//vector <int> v; 空数组
#include<vector>
#include<iostream>
using namespace std;
int main(){
	vector <int> v; 
//空数组

//分配数组大小v.resize(length)
	v.resize(10);
	cout<<v.size()<<endl;
//显示大小
	for(int i=0;i<10;i++){
		v[i]=i;}
	for(int j=0;j<10;j++){
		cout<<v[j]<<" ";}
//遍历赋值 输出

//追加元素
	v.push_back(11);
	for(int k=0;k<11;k++) 
		cout<<v[k]<<" ";
//将11放入v并且添加空间
	return 0;
}
```

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main(){
	vector <int> v(10,2);
//分配了10个空间 每个空间都初始化为2
	for(int i=0;i<10;i++)
	cout<<v[i]<<" ";
	cout<<endl;
	v.resize(2);
//resize后只有多出来的空间会变成0 如果旧大小>=新大小 则只改变空间不改变值
	for(int k=0;k<2;k++)
        cout<<v[k]<<" ";
        cout<<endl;

	vector <int> u(10);
//分配了十个空间全都初始化为0
	for(int j=0;j<10;j++)
	cout<<u[j]<<" ";
	cout<<endl;
//遍历一遍 不考虑开头与结束
	v.push_back(12);
	for(auto p=v.begin();p!=v.end();p++)
//v.end()指向最后一个元素后面
	cout <<*p<<" ";
	cout<<endl;
}
//set集合元素互不相同 元素会按照从小到大排序
//插入遍历查找删除
```

```cpp
#include<iostream>
#include<set>
#include<vector>
using namespace std;

int main(){
	set <int> s;
//不可加参数 分配空间也不可行
//	vector <int> v(10,2);

//插入元素
	s.insert(4);
	s.insert(2);
	s.insert(1);
	for(auto p=s.begin();p!=s.end();p++)
		cout<<*p<<" ";
//读取指针指的元素
	cout<<endl;
//输出1 2 4

//查找
	cout<<(s.find(2)!=s.end())<<endl;
	cout<<(s.find(5)!=s.end())<<endl;
//分别输出1 0表示true false
//	加了括号是布尔值
//	s.find()的返回值是指针
//s.find执行一次查找 找到了就返回所找元素的迭代器 没找到就返回s.end()（末尾迭代器）

//删除元素
	s.erase(1);
	cout<<(s.find(1)!=s.end())<<endl;
//输出0表示false
return 0;
}
//map键值对 它会自动将所有键值对按照键从小到大（ASCII）排序
//创建键值对eg. map <string,int> m;
//添加 访问 遍历 获取长度
```

```cpp
#include<iostream>
#include<map>
using namespace std;
int main(){
	map <string,int> m;
//添加
	m["hello"]=2;
	m["fuckyou"]=3;
//访问
	cout<<"hello: "<<m["hello"]<<endl;
//遍历：迭代器 获取值时类似的结构体指针
	for(auto p=m.begin();p!=m.end();p++)
		cout<<p->first<<":"<<p->second<<endl;
//m.begin()是结构体指针
/*类似这种
struct m
{
	string key;
	int data;
};
*/
//获取长度 m.size()  stack queue 都可以获得长度
	cout<<"the length of map:"<<m.size()<<endl;
//输出键的个数
return 0;
}
//栈只允许在表的一段进行插入、删除操作的线性表
//有口无肛门
//栈stack先进后出 queue队列先进先出
//创建栈stack <元素类型> s
//处理 压栈 出栈 访问栈顶 获取长度
```

```cpp
#include<iostream>
#include<stack>
using namespace std;
int main(){
//创建栈
	stack <int> s;
//压栈
	s.push(1);
	s.push(2);
	s.push(3);
//先放1 再放2、 3
	cout << s.top() <<endl;
//输出栈顶3

//出栈
	s.pop();
	cout<<s.top()<<endl;
//输出2

//获取长度
	cout << "栈的长度为："<<s.size()<<endl;
//遍历不可行 栈没有begin 方法 无法获取除了栈顶外的元素
//	for(auto p=s.begin();p!=s.end();p++)
//		cout<<*p<<endl;
return 0;
}
//队列 有口有肛门 先进先出
```

```cpp
#include <queue>
#include <iostream>
using namespace std;
int main(){
	queue <int> q;
//入队
	for(int i=1;i<=10;i++)
		q.push(i);
//可获取队首队尾元素
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

//出队
	q.pop();
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

	q.push(11);
	cout<<"队首为："<<q.front()<<endl<<"队尾为："<<q.back()<<endl;

//获取长度
	cout<<q.size()<<endl;
return 0;
}
//unordered_map unordered_set
//无序map set 省去了排序的过程 如果刷题的时候超时了 可以使用
//操作和有序的相同
```
```cpp
#include<iostream>
#include<unordered_map>
#include<unordered_set>
using namespace std;
int main(){
	unordered_map <string,int> m;
	unordered_set <int> s;
	s.insert(1);
	s.insert(2);
	s.insert(3);

	m["hello"]=1;
	m["world"]=2;
	m["fuck"]=3;
	cout<<"集合中的元素为：";
	for(auto p=s.begin();p!=s.end();p++)
		cout<<*p<<" ";
	cout<<endl;
	for(auto p=m.begin();p!=m.end();p++){
		cout<<"key:"<<p->first<<" value:"<<p->second<<" ";
		cout<<endl;}

return 0;
}
//输出顺序和哈希表有关
//位运算 bitset
//用于处理二进制
//类似字符数组
//bitset从低位到高位存储 打印和初始化的时候看到的是从高位到低位
//bitset<8> b(0b10101010);
//内存中的存储
//索引:0 1 2 3 4 5 6 7
//位： 0 1 0 1 0 1 0 1
//  最低位         最高位
//打印出来 cout<<b<<endl;  //10101010索引7到索引1打印
//打印和初始化 与 存储和访问相反
//bitset<5>b(u) u为unsigned int如果u=1,输出b的结果为00001
//bitset<8> b(s) s为字符串 如"1101"  则输出b的结果为00001101
```
```cpp
#include<bitset>
#include<iostream>
using namespace std;
int main(){
//初始化
	bitset <5> b(19);
	cout<<b<<endl;//10011
	for(int i=0;i<b.size();i++){
	cout<<b[i]<<endl;
	}
	bitset <5> c("11");
	cout<<c<<endl;//00011
//bitset <5> b;表示5个二进制位 初始化为00000
//(19)意为该二进制数字转换成十进制时为19 即(2)_2=(19)_19    ?=10011



//处理
//b.any()是否有1
	cout<<"是否有1:"<<b.any()<<endl;
//b.none()是否不存在1
	cout<<"是否不存在1:"<<b.none()<<endl;
//b.count "1"的个数
	cout<<"b中1的个数:"<<b.count()<<endl;
//b.test(i) 下标为i的元素是不是1
	cout<<"下标为0的元素是不是1:"<<b.test(0)<<endl;
//b.size()  b中元素的个数
	cout<<"b中元素的个数:"<<b.size()<<endl;
//b.flip()取反 1改0 0改1 所有位置取反
	cout<<b.flip()<<endl;
//b.flip(i) 第i位取反
	cout<<b.flip(0)<<endl;
//所有位置归0 b.reset()
//第i位归0 b.reset(i)
//转换为Unsigned long类型 
//unsigned long a=b.to_ulong();
	unsigned long a = b.to_ulong();
	cout<<a<<endl;


//bitset<5>b(s,pos,n)  从字符串s[pos]开始 读取n位长度进b
	string m="0110101";
	bitset <5> d(m,0,5);
	cout<<d<<endl;
//01101
//等效于 
//bitset <5> d("01101");
return 0;
}
//sort()函数
//主要功能是对一个数组int arr[] 或者 vector进行排序 vector是容器 需要用begin end表示头尾
//arr[]使用 arr表示数组首地址 arr+n表示尾部
```

```cpp
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	vector <int> m(10);
	for(int i=9;i>=0;i--)
		m[i]=10-i;
	for(int k=0;k<10;k++)
		cout<<m[k]<<" ";
	cout<<endl;
	m.push_back(-1);
	sort(m.begin(),m.end());
//sort(开始排序的地方,结束排序的地方,cmp) 不一定是头尾 可以是中间部分排序
//从小到大排序
	for(int j=0;j<11;j++)
		cout<<m[j]<<" ";
	cout<<endl;
//sort()默认从小到大排序 但是使用cmp可以自定义一些规则compare

}
//sort()默认从小到大排序 但是使用cmp可以自定义一些规则compare
```

```cpp
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
bool cmp(int x,int y){
	return x>y;
}
//bool 类型函数 如果返回true x排在y前面 如果返回false y排在x前面
//不能有等于
int main(){
	vector <int> v;
	for(int i=1;i<=10;i++)
		v.push_back(11-i);
	for(auto p=v.begin();p!=v.end();p++)
		cout<<*p<<" ";
	cout<<endl;
//从大到小push进去
		sort(v.begin(),v.end());

		for(auto p=v.begin();p!=v.end();p++)
			cout<<*p<<" ";
			cout<<endl;
//从小到大
//使用cmp

		sort(v.begin(),v.end(),cmp);
		for(int i=0;i<10;i++)
		cout<<v[i]<<" ";
		cout<<endl;

return 0;
}
//在sort内部如果cmp为真 则顺序不变 如果为假 则交换
```

```cpp
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
struct stu
{
	string name;
	int age;
};
bool cmp(stu a, stu b)
{
	if(a.age!=b.age)
		return a.age<b.age;
	else
		return a.name<b.name;
}
//年龄不相等从小到大排序 否则按照名字的字典序
int main(){
	stu s[3];
	for(int i=0;i<3;i++)
		cin>>s[i].name>>s[i].age;
//tom 19
//mike 20
//tt 12

	sort(s,s+3,cmp);
	for(int i=0;i<3;i++)
		cout<<s[i].name<<" "<<s[i].age<<endl;

	return 0;
}
```

```cpp
#include<cctype>
//C语言的#include<ctype.h>
#include<iostream>
using namespace std;
int main(){
	char c = 'A';

cout<<"isalpha:"<<isalpha(c)<<endl;//判断是否是字母
cout<<"islower:"<<islower(c)<<endl;//判断是否小写字母
cout<<"isupper:"<<isupper(c)<<endl;//判断是否大写字母
cout<<"isalnum:"<<isalnum(c)<<endl;//判断是否是字母or数字
cout<<"isspace:"<<isspace(c)<<endl;//判断是否是空格 \t \r \n
//布尔类型
//其实是int类型 但是可以将非0理解为true 理解为false就行了
char s=tolower(c);//转化成小写字母
cout<<s<<endl;
char s1=toupper(c);
cout<<s1<<endl;
return 0;

}
//c++11的解释 新增 auto to_string() stoi stof unordered_map unordered_set
```




```cpp
#include<iostream>
#include<vector>
using namespace std;
int main(){
//auto声明
//auto x=19;自动识别数据类型
//auto float y=1.8;
//不可
//auto a;
//cin>>a;
//需要直接初始化
//不过可以cin>>n;  auto a=n;

//迭代器
vector <int> a(10,1);
for(auto p=a.begin();p!=a.end();a++)
	cout<<*p<<" ";
return 0;
}
//数组可用迭代器
//集合可用
//键值对遍历可用 获取值时类似结构体指针
//栈只可访问栈顶 队列只可访问队首队尾 不可用
//unordered也可
```



```cpp
#include<iostream>
#include<vector>
using namespace std;
//基于范围的for 循环
//传值 for(int i:arr) cout<<i<<endl;   输出数组中的每一个元素的值 不能改变元素的值
//传址 for(int &i:arr) i=i*2;               将数组中的每一个元素都*2 只有在引用的时候才能改变元素的值
//推广 for(auto i:v) cout<<i<<" ";       这里的v是一个vector其实所有的容器都可以使用这种方式循环（配合auto）

int main(){
	int a[5]={1};//1 0 0 0 0
	for(int i:a)//用i访问a
		cout<<i<<" ";
//输出a[i]   有点像python 的for i in a
	cout<<endl;

	for(int i:a)
		i++;

	for(int i:a)
		cout<<i<<" ";
//1 0 0 0 0
//传值调用 不改变值
	cout<<endl;
	
	int b[5]={1};
	for(int &i:b)
		i++;
	for(int i:b)
		cout<<i<<" ";

//传址调用


	vector <int> c(10,1);
	for(auto i:c)//改int也可正常输出
		cout<<i<<" "
return 0;
}
```















makefile
makefile is a tool to simplify and organize compilation
It is a set of commands with variable names and targets
you can compile a project or only the update files in the project by using makefile
A rule of makefile includes three elements: targets, prerequisites and commands.
targets:prerequisites
<TAB> command
The target can be an object file, which will be generated by the command
The prerequisites are file names, separated by spaces. The targets generation depends on the prerequisites
The commands will be run to generate targets. These need to start with a tab!
Lab
如果有大量文件需要编译 全部一起g++ -o将会花费大量时间
可以逐个编译 g++ -c只编译不连接 最后g++ *.o -o ...
命令可以写成脚本文件makefile!
在Makefile文件中输入
eg.
终端输入make 会自动寻找目录下的makefile 文件
|____factorial.cpp
|____functions.h
|____main.cpp
|____Makefile
|____printhello.cpp

## VERSION1
hello: main.cpp printhello.cpp factorial.cpp
	g++ -o hello main.cpp printhello.cpp factorial.cpp
如果hello比cpp文件都要“新” 则再次make不会生成任何东西
但是如果有一个文件在hello生成之后修改了make 会重新生成一个hello
文件太多了的话 输入会很麻烦

## VERSION2
CXX=g++
TARGET=hello
OBJ=main.o printhello.o factorial.o

$(TARGET):$(OBJ)
	$(CXX) -o $(TARGET) $(OBJ)
main.o:main.cpp
	$(CXX) -c main.cpp
printhello.o:printhello.cpp
	$(CXX) -c printhello.cpp
factorial.o:factorial.cpp
	$(CXX) -c factorial.cpp

只编译修改过的文件


##VERSION3
CXX=g++
TARGET=hello
OBJ=main.o printhello.o factorial.o

CXXFLAGS=-c -Wall

$(TARGET):$(OBJ)
	$(CXX) -o $@ $^
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f *.o $(TARGET)
@为TARGET 即目标生成文件  ^为OBJ 即依赖

##VERSION4
CXX=g++
TARGET=hello
SRC=$(wildcard *.cpp)
OBJ=$(patsubst %.cpp,%.o,$(SRC))

CXXFLAGS=-c -Wall

$(TARGET):$(OBJ)
	$(CXX) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f *.o $(TARGET)

## 🎯 Makefile 是什么？

**Makefile 就是一张"编译说明书"**，告诉电脑：
- 先编译哪个文件
- 后编译哪个文件
- 最后怎么把它们拼成一个程序

---

## 🤔 为什么要用它？

假设你有 3 个文件：`main.cpp`、`game.cpp`、`player.cpp`

### 不用 Makefile（手打命令）
```bash
g++ -c main.cpp
g++ -c game.cpp
g++ -c player.cpp
g++ -o game main.o game.o player.o
```
每次改完代码都要敲一遍，**文件多了能累死人**。

### 用 Makefile（自动化）
```makefile
game: main.o game.o player.o
	g++ -o game main.o game.o player.o

main.o: main.cpp
	g++ -c main.cpp

game.o: game.cpp
	g++ -c game.cpp

player.o: player.cpp
	g++ -c player.cpp
```
然后只需要敲：
```bash
make
```
它就**自动帮你编译所有改过的文件**，没改过的就不编译（省时间）。

---

## 📝 Makefile 的"公式"

```makefile
目标: 依赖1 依赖2
	命令
```

- **目标**：要生成的东西（比如 `game` 或 `main.o`）
- **依赖**：生成目标需要哪些文件
- **命令**：怎么生成（前面必须按 **Tab 键**缩进）

---

## 🔍 举个生活的例子

想象你要做一份**三明治**：

| Makefile 写法 | 真实世界 |
| :--- | :--- |
| `三明治: 面包 生菜 火腿` | 三明治需要面包、生菜、火腿 |
| `Tab + 组装三明治的命令` | 把它们叠在一起 |
| `面包: 面粉 水 酵母` | 面包需要面粉、水、酵母 |
| `Tab + 烤面包的命令` | 放进烤箱烤 |

Makefile 就是在告诉电脑：**"想做三明治？那先检查面包、生菜、火腿有没有，没有就先做，最后组装。"**

---

## 🎮 你现在游戏项目的 Makefile 示例

```makefile
# 目标文件名
TARGET = game

# 所有源文件
SRCS = main.cpp game.cpp player.cpp

# 编译规则
$(TARGET): $(SRCS)
	g++ -std=c++17 -o $(TARGET) $(SRCS)

# 清理
clean:
	rm -f $(TARGET)
```

保存为 `Makefile`，然后：
```bash
make      # 编译
./game    # 运行
make clean  # 删除编译出来的文件
```

---

## 📊 总结

| 问题 | 答案 |
| :--- | :--- |
| **Makefile 是什么？** | 编译说明书，告诉电脑怎么编译代码 |
| **为什么用它？** | 自动编译、省时间、只重编译改过的文件 |
| **核心结构？** | `目标: 依赖` + `Tab 命令` |
| **怎么运行？** | 终端敲 `make` |
| **和你啥关系？** | 你的游戏项目可以用 Makefile 方便编译 |

---

**一句话**：Makefile 就是帮你**自动编译代码**的脚本，省得你每次手动敲命令。写完 Makefile 后，以后只需要 `make` 就完事了！🎯






cmake
makefile依赖于平台
cmake不依赖
cmake的comments begins with #
创建一个文件
CMakeLists.txt
写入

cmake_minimum_required(VERSION 3.10) 
#版本选择根据需求定

project(hello)

add_executable(hello main.cpp factorial.cpp printhello.cpp)



#如果文件太多 可以在add_executable前添加
aux_source_directory(<dir> <variable>)
The command finds all the source files in the specified directory indicated by <dir> and stores the results in the specified variable indicated by <variable>
自动查找指定目录下的所有源文件 并把文件名列表存到一个变量里
aux_source_directory(src SOURCES)
add_executable(hello ${SOURCES})
终端运行
cmake .

产生
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sleepysloth/note/learning_note/cppex/makefileex

这样会产生很多文件
可以创建一个build目录并且进入
输入cmake ..
即可


## 🎯 CMake 是什么？

**CMake 是一个"自动生成 Makefile 的工具"**。

你不是刚学了 Makefile 吗？CMake 就是帮你**自动写 Makefile** 的，不用你手写。

---

## 🤔 为什么要用 CMake？

手写 Makefile 有两个麻烦：

1. **麻烦**：几个文件还好，几十上百个文件写起来要命
2. **不通用**：Windows、Linux、macOS 的编译方式不同，Makefile 没法直接跨平台

CMake 解决了这两个问题：
- **自动生成**：几行配置，自动生成完整的 Makefile
- **跨平台**：在不同系统上都能生成对应的构建文件（Windows 上还能生成 Visual Studio 项目）

---

## 📝 怎么用？

### 1. 写一个 `CMakeLists.txt`（CMake 的配置文件）

```cmake
cmake_minimum_required(VERSION 3.10)  # 指定 CMake 最低版本
project(MyGame)                        # 项目名字

set(CMAKE_CXX_STANDARD 17)             # 使用 C++17

add_executable(game                     # 要生成的可执行文件名
    main.cpp                            # 源文件1
    game.cpp                            # 源文件2
    player.cpp                          # 源文件3
)
```

就这么几行，比手写 Makefile 简单多了吧？

### 2. 运行 CMake（"外部构建"，推荐）

```bash
mkdir build          # 创建一个干净的构建目录
cd build
cmake ..             # 自动生成 Makefile（在 build/ 里）
make                 # 用 Makefile 编译
```

**注意**：`cmake ..` 是在告诉 CMake："去上一级目录找 `CMakeLists.txt`"。

---

## 🔍 完整流程对比

### 不用 CMake（手写 Makefile）
```
手写 Makefile → make → 可执行文件
```

### 用 CMake
```
写 CMakeLists.txt → cmake → 自动生成 Makefile → make → 可执行文件
```

多了一步 `cmake`，但省了手写 Makefile 的功夫。

---

## 🎮 你的游戏项目用 CMake

```
你的项目文件夹/
├── CMakeLists.txt    ← 你写这个
├── main.cpp
├── game.cpp
└── player.cpp
```

**CMakeLists.txt**：
```cmake
cmake_minimum_required(VERSION 3.10)
project(Game)

set(CMAKE_CXX_STANDARD 17)

add_executable(game main.cpp game.cpp player.cpp)
```

然后编译：
```bash
mkdir build && cd build
cmake ..
make
./game    # 运行
```

---

## 📊 Makefile vs CMake

| 对比 | Makefile | CMake |
| :--- | :--- | :--- |
| **角色** | 直接告诉编译器怎么做 | 生成 Makefile |
| **谁写的** | 你手写 | CMake 自动生成 |
| **跨平台** | ❌ 要自己适配 | ✅ 自动适配 |
| **语法** | 复杂（Tab 缩进、规则难记） | 简单（像写配置） |
| **大型项目** | 难维护 | 轻松管理 |

---

## 💡 一句话总结

> **CMake = 自动生成 Makefile 的工具，让你不用手写 Makefile，还能跨平台。**

写一个 `CMakeLists.txt`，然后 `cmake` + `make` 就完事了。现代 C++ 项目基本都用它，包括你听过的大项目（LLVM、OpenCV、Qt 等）。🎯

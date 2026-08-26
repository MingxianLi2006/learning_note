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

%常用函数
%abs mod sqrt exp

clear;
clc;
x=-5;
abs(x)%求复数的模
y=1+5i;
abs(y)
mod(11,3)%取模
sqrt(1+i)
sqrt(1:9)

format long
sqrt(-5)

exp(i*pi/8)

%log() log2() log10() 计算以e 2 10为底的对数
%round() 四舍五入
%round(1.1)
%round(3.14159,1) 四舍五入保留一位小数
%round(314.15926,-1)  保留两位整小数 0的话保留整数



%三角函数
%sin() asin()反正弦 以弧度为单位 asind()以角度为单位

%isempty函数
%如果A为空数组isempty(A)返回1 否则.
%等价于length(A)==0
A=[1:9];
x=[2:10];
find(x==A)

%%meshgrid函数基于向量x和y中包含的坐标来返回二位网络坐标
 x=0:4;
 y=0:5;
 [xx,yy]=meshgrid(x,y)%x,x也行
 z=xx.^2+yy.^2

 %rng函数 用来设置随机数种子 能生成可重复的随机数
 %使用在随机数生成函数(rand,randi)之前 使用rng(seed)命令设置随机数种子
 %%
 seed=3;
 rng(seed)
 randi([5 10],3,3)
 randi([3,10],5,5)
%%
A=0:10
B=10:15
ismember(A,B)
%A中的元素是否存在于B？
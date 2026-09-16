clc;
clear;
%结构基础 
% 条件结构 if elseif elseif else end
%%
score=87;
if (score>=90) && (score<=100)
    res=1;
elseif(score>=80) && (score<90)
    res=2;
elseif(score>=60) && (score<=80)
    res=3;
elseif(score>=0) && (score<=60)
    res=4;
else
    res=0;
end
res
%if [1,2;0,1] 这个矩阵会被转化为布尔值0 1的话需要矩阵所有值非零
%if any(A(:)) 只要A中有一个非零元素 条件都成立
%每个if都要有配套的end
a=10;
b=20;
c=15;
if(a>b)
    if(a>c)
        max=a;
    else
        max=c;
    end
else
    if b>c
        max=b;
    else
        max=c;
    end
end
max;

%%swich-case-otherwise-end
season=randi([1,4]);
switch season
    case 1
        disp("Spring");
    case 2
        disp("Summer");
    case 3
        disp("Autumn");
    otherwise
        disp("Winter")
end

%%循环结构
%for-end
for i=1:5
    i
end

A=randi([-3,3],2,3)
for i=A
    i
end
%遍历了矩阵的每一列

x=1:6
res_sum=0;
for i=x
    res_sum=res_sum+i;
end
res_sum
%断点 步进

%%求1~9999年间 有多少个闰年
count=0;
for x=1:9999
    if(mod(x,4)==0 && mod(x,100)~=0) || (mod(x,400)==0)
        count=count+1;
    end
end
count
%%while-end
F(1)=1;F(2)=1;
n=2;
while(F(n)<=9999)
    n=n+1;
    F(n)=F(n-1)+F(n-2);
end
   n
   F(n)
%break continue

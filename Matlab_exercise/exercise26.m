clear;
clc;
x=[1:0.1:9];
y=x.^2;
plot(x,y);
%%
x=[0.5:0.2:2.1];
y=[0.1:0.2:1.7];
X=x+y*i
plot(X)

%当XY为矩阵
t=0:0.01:2*pi;
t=t.';
x=[t,t,t];
y=[sin(t),sin(2*t),sin(0.5*t)];
plot(x,y);
%plot(X,Y,LineSpec)可指定线型 标记和颜色
%plot(x1,y1,...,xn,yn)在同一组坐标轴上绘制多对x y
%上面每一个yn后面可以加一个LineSpec
%'-'实线 '--'虚线 '：'点线 '-.'点划线 还可以加颜色符号
%%绘制多个曲线
x1=linspace(0,2*pi,10);
x2=linspace(0,2*pi,20);
x3=linspace(0,2*pi,100);
y1=sin(x1);
y2=sin(x2)+2;
y3=sin(x3)+4;
plot(x1,y1,'red',x2,y2,x3,y3);

%%fplot函数
%fplot(f)在默认区间[-5,5]绘制由函数y=f(x)定义的曲线
%fplot(f,interval)
x=[0:0.005:0.2]
z=sin(1./x);
fplot(@(x)sin(1./x),[0,0.2])
plot(x,z)

%%fplot(funx,funy)在默认区间[-5,5]绘制由x=funx(t)和y=funy(t)定义的曲线
%后面可以加上interval
%参数方程
fplot(@(t)t*sin(t),@(t)t*cos(t),[0,10*pi],'-r')

%其他坐标系的二维曲线
%对数坐标图
%semilogx(x,y)在x轴上以10为底的对数刻度、在y轴上使用线性刻度来绘制x和y
%要绘制由线段链接的一组坐标 要将x y指定为相同长度的向量
%要在同一坐标区上绘制多组坐标 要将xy中的至少一个指定为矩阵
%后面可以加LineSpec

x=logspace(-1,2);%0.1到100
y=x;
semilogx(x,y);

%极坐标图
%polarplot(theta,rho)在极坐标中绘制线条 向量长度要相等
t=[0:0.001:4*pi];
r=(sin(t)).^t;%注意这里t是一个向量 
polarplot(t,r);

%%统计图
%条形图
%bar(y)创建一个条形图 y中的每个元素对应一个条形
%要绘制单个序列要将y指定为长度为m的向量
%要绘制多个条形序列 将y指定为矩阵 每个序列对应一列
%bar(x,y)在x指定的位置绘制条形


x=[2021:1:2023];
y=[10,20;20,30;100,200];
bar(x,y)


%直方图
%histogram(X)基于X创建直方图 使用自动分bin算法 然后返回均匀宽度的bin
%bin可覆盖X中的元素范围并显示分布的基本形状
%histogram将bin显示为矩形条 每个举行的高度就表示bin中元素数量
%histogram(X,nbins)指定bin的数量 即区间数量
x=randn(1000,1)%1000*1矩阵
histogram(x,10)
%获取bin的计数
h=histogram(x,10);
counts=h.Values

%面积类图形
%pie(X)使用X中的数据绘制饼图 饼图中的每个扇区代表X中的一个元素
%如果sum(X)<=1 X中的值直接指定饼图扇区的面积 如果<1 仅绘制部分饼图
%如果>1 则进行归一化处理
%如果X为categroical数据类型 则扇区对应于类别 每个扇区的面积是类别中的元素除以X中元素数的结果
%pie(X,explode)将扇区从饼图偏移一定位置 explode是一个由X对应的零值和非零值组成的向量或者矩阵
%pie函数仅将对应于explode中的非零元素的扇区便宜一定位置
%如果X为categorical数据类型 则explode可以是由对应于类别的零值和非零值组成的向量 或是要偏移的类别名称组成的元胞数组

x=[1:2:9];
pie(x)

X=categorical({'North','South','North','East','South','West'});
explode={'West','East'};
labels={'E','N','S','W'};
pie(X,explode,labels)

%散点类图形
%scatter(x,y) 在向量x和y指定的位置创建一个包含圆形标记的散点图
%要绘制一组坐标 xy要等长
%多组坐标其中一个要是矩阵
%scatter(x,y,sz)可指定圆圈大小 所有圆圈大小相等 sz为标量 否则为向量或者矩阵
%scatter(x,y,sz,c) 颜色的指定同上
% scatter...,"filled")填充圆
% scatter(...,mkr)指定标记类型

%%画一颗爱心
t=0:pi/50:2*pi;
x=16*sin(t).^3;
y=13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
scatter(x,y,'red','filled')

%%矢量类图形
%quiver(X,Y,U,V)在由XY指定的笛卡尔坐标上绘制具有定向分量UV的箭头  （X，Y）->(U,V)
%第一个箭头源于X(1)Y(1)按U(1)水平延伸 V(1)垂直延伸 默认quiver缩放箭头长度使其不重叠
%quiver(U,V)在等距点上绘制箭头，箭头的定向分量由UV指定
%UV为向量 则箭头的x坐标范围是1到U和V中的元素数 y坐标为1
%UV为矩阵 箭头x的坐标范围是从1到U和V中的列数 箭头y坐标范围是从1到U V中的行数
A=[4,5];
quiver(0,0,A(1),A(2));
B=[1:1:10]
C=[11:1:20]
quiver(B,C)

%图形属性设置
%线型 标记和颜色
%指定为包含符号的字符串标量或字符向量 符号可以任意顺序显示
%"--or"为带有圆形标记的红色虚线
%'-'实线 '--'虚线 ':'点线 '-.'点划线
%标记'o' '+' '*' '.' 'x' '_' '|' 'square' 'diamond' '^' '>' '<' 'pentagram'
%'hexagram'
%颜色名称  'red' 'r'  'green' 'g'    'blue' 'b'
%'cyan'  'c'淡蓝色   'magenta' 'm'   'yellow' 'y'
%'black' 'k'  'white' 'w'  也可以用RGB三元组

%图形标注
%都支持LaTeX
%title(图形标题) 
%xlable(x轴说明) ylable(y轴说明) text(x,y,图形说明)  legend(图例1,图例2...)
 
%坐标控制
%axis函数 指定当前坐标区范围
%axis([xmin,xmax,ymin,ymax,zmin,zmax])指定当前坐标区范围

%axis equal:横坐标采用等长刻度
%axis square正方形坐标系
% axis auto 使用默认设置
%axis off 取消坐标轴
%axis on显示坐标轴

%给坐标系加上网格边框
%grid on:控制显示网格线 off则不显示
%默认无网格线

%%属性设置
x=linspace(0,2*pi,200);
y=[sin(x);sin(2*x);sin(0.5*x)];
plot(x,y);
axis([0,4,-1.5,1.5]);
title('three sine curvey=sin{\theta}','FontSize',24)%FontSize让title变大
xlabel('X');
ylabel('Y');
text(2.5,sin(2.5),'sin(x)');
text(2.5,sin(2*2.5),'sin(2x)');
text(2.5,sin(0.5*2.5),'sin(0.5x)');
%跟画图的时候元素位置一样
legend('sin(x)','sin(2x)','sin(0.5x)')

% %图形保持
% hold on:控制保持原有图形
% hold off:控制刷新图形窗口
% hold on:用于在两种状态之间切换

%画同心圆
t=linspace(0,2*pi,200);
x=sin(t);
y=cos(t);
plot(x,y,'b');
axis equal;
hold on 
axis square
x1=2*sin(t);
y1=2*cos(t);
plot(x1,y1,'r')
%%两个向量相加
axis auto;
A=[4,5];
B=[-10,10];
C=A+B;
hold on;
quiver(0,0,A(1),A(2));
quiver(0,0,B(1),B(2));
quiver(0,0,C(1),C(2));
legend('A','B','A+B');
title("The result of A+B")
xlabel('X')
ylabel('Y');
text(A(1),A(2),'A');
text(B(1),B(2),'B');
text(C(1),C(2),'C');
grid on;
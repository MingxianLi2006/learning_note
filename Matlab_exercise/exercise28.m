%三维曲面
%平面网格数据的生成
%利用矩阵运算或者 meshgrid函数生成[X,Y]=meshgrid(x,y)
%参数x y为向量 存储网格点坐标的X Y为矩阵
x=[2:6];
y=[3:8]';
X=ones(size(y))*x  %六维全为1的列向量*x
Y=y*ones(size(x))
%等价于
[X,Y]=meshgrid(x,y);
%绘制三维曲面的函数
%mesh(x,y,z,c);
%surf(x,y,z,c); 其中x,y为网格坐标矩阵z为网格点的高度矩阵 c用于指定不同高度下曲面的颜色 
%无c则默认颜色正比于图形的高度
x=[-1:0.1:1];
y=[-1:0.1:1];
[X,Y]=meshgrid(x,y);
Z=X.*exp(-X.^2+Y.^2);
plot3(X,Y,Z);
mesh(X,Y,Z);%三维曲面
surf(X,Y,Z)
shading interp;

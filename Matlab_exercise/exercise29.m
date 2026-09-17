%x,y为两个向量 使用meshgrid 函数生成对应的平面网格
%Z可以时任意值 绘制空间曲线
x=[2:0.1:6];
y=[3:0.1:8];
[X,Y]=meshgrid(x,y);
%扩展生成6*5矩阵
Z=randn(size(X));
plot3(X,Y,Z)
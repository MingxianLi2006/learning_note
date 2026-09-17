format('default')
rng default
%二维图形绘制
%基本绘图函数
%plot函数
%plot(X,Y) 创建Y中数据对X中对应值的二维线图
%数据量一样

x=[0,9];
y=[1,10];
plot(x,y); %画出了一一对应的直线
%%
format("default");
z=[1:9];
w=z.^2;
plot(z,w);
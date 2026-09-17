%三维曲线
%plot3(x,y,z) fplot3 

clc;clear;
%绘制螺旋线
hold off;
t=linspace(0,10,10000);
x=sin(t)+t.*cos(t);
y=cos(t)-t.*sin(t);
z=t;
plot3(x,y,z)

% t=linspace(-10,10,10000);
% x=sin(t)
% y=cos(t);
% z=t;


%%plot3(x1,y1,z1,x2,y2,z2,...)
%对于plot3函数来讲 它的参数可以不止是1D数组
%x,y,z为同型矩阵时 以x,y,z对应列元素绘制曲线 曲线条数等于矩阵列数
%参数xyz中有向量 也有矩阵时 向量的长度和矩阵相符

t=t.';
x=[t,t,t];
y=[sin(t),sin(t)+2,sin(t)+4];
z=t;
plot3(x,y,z);
xlabel('X')
ylabel('Y')
zlabel('Z')

%fplot3(funx,funy,funz,tlims)
x=@(t)exp(-t./10).*sin(5.*t);
y=@(t)exp(-t./10).*cos(5.*t);
z=@(t)t;
fplot3(x,y,z,[-12,12],'-r');


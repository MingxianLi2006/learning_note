%句柄/窗口控制（子图）
%句柄可以理解为一个引用或者指针用来代表某个对象 通过句柄可以访问操作对象

%对象句柄值的获取
%句柄引用图形图像的具体实例
%使用对象句柄设置和查询对象属性的值，对象 句柄值 类似于编程时的引用
%将对象的句柄值赋值给变量后 该变量可以代表指定的绘图对象
%当创建图形对象时 可以将对象的句柄保存在变量中
x=1:10;
y=x.^2;
h=plot(x,y);%h是这个图形的句柄
h1=text(5,25,'说明');
h1.FontSize=24;

%图形对象句柄及属性
% 对象句柄的获取
% 句柄变量是对象 不要将句柄转换为其他类型
%需要转换为逻辑值
%对象属性的获取/设置
% 获取某个对象的属性：使用get函数 
% 设置某个对象的属性：使用set函数 

x=linspace(0,2*pi,100);
y=sin(x);
h=plot(x,y);
get(h)

set(h,'Color','red')

%图形窗口的分割
%子图：同一图形窗口中的不同坐标系下的图形为子图
%subplot(m,n,p) m n指定将图形窗口分成m*n个绘图区 p指定当前活动区
x=linspace(0,2*pi,100);
subplot(2,2,1); %激活第一块小区域
fplot(@(x)sin(x));
title('sin(x)');



subplot(2,2,2)
plot(x,cos(x));
title('cos(x)')




subplot(2,2,3);
plot(x,tan(x));
title('tan(x)')


subplot(2,2,4);
fplot(@(x) cot(x));
title('cot(x)')

%%分别用mesh surf plot3绘制z=x e^-(x^2+y^2)
x=[-3:0.1:3];
y=[-3:0.1:3];
[X,Y]=meshgrid(x,y);
Z=X.*exp(-(X.^2+Y.^2));
subplot(1,3,1);
mesh(X,Y,Z);
title('mesh function')

subplot(1,3,2);
surf(X,Y,Z);
title('surf function')
%去掉黑线 平滑着色
shading interp;
axis tight;

%mesh只有网格线 面片透明
%surf用颜色填充小面片 默认有黑边

%可以用 figure命令  或者  figure(1)   figure(2)这种生成多个窗口


subplot(1,3,3);
plot3(X,Y,Z);
title('plot3 function')
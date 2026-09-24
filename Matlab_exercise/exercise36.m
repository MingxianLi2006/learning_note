figure(1)

t=linspace(0,100,10000);

x=cos(t);

y=sin(t);

plot3(x,y,t);
%%picture2
figure(2)

x=linspace(0,2*pi,10000);

y=2*exp(-0.5.*x).*cos(4*pi.*x);

plot(x,y)

figure(3)

fplot(@(x)2*exp(-0.5*x)*cos(4*pi*x),[0,2*pi]);
hold on;
%%
figure(4)
x=[1+1i,2+1i,3+1i];

plot(x,"k--");


%%plot函数 当x y为同维矩阵时，回忆x,y对应的列元素为横纵坐标分别绘制曲线，曲线


%%

figure(5)
x=linspace(0,2*pi,1000);
y1=0.2*exp(-0.5*x).*cos(4*pi*x)
plot(x,y1);
hold on

y2=2*exp(-0.5*x).*cos(pi*x)
plot(x,y2);
k=find(abs(y1-y2)<1e-2);
x1=x(k)
y3=0.2*exp(-0.5*x1).*cos(4*pi*x1)
plot(x1,y3,'bp');
text(x1,y3,"I")
legend("curve1","curve2")       %加图例
title("I just fucking destory them")
xlabel("xxx")
ylabel("yyy")       %加y轴说明
text(0.3,0.5,'sin({\omega}t+{\beta})')      %加文本说明
box on      %加边框
grid on     %网格线
axis equal  %等刻度线
%%
figure(6)
x=linspace(0,2*pi,10000);
y=sin(x);
z=cos(x);
t=sin(x)./(cos(x)+eps);
ct=cos(x)./(sin(x)+eps);
subplot(2,2,1);
plot(x,y);
title('sinx')
subplot(2,2,2);
plot(x,z);
title('$\cos x$','Interpreter','latex')
subplot(2,2,3);
plot(x,t);
axis([0 2*pi -40 40]);
title("$\tan x$",'Interpreter',"latex")
subplot(2,2,4);
plot(x,ct);
title("$cot x$",'Interpreter','latex')
axis([0 2*pi -40 40])
sgtitle("for fundamental triangular functions")
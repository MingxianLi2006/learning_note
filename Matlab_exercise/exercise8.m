x1=linspace(0,4*pi,10000);
x2=linspace(0,4*pi,10000);
x=[x1,x2]';
y1=0.5*x1.*cos(4*pi*x1);
y2=2*exp(-0.5*x2).*cos(pi*x2);
y=[y1,y2];
plot(x,y)
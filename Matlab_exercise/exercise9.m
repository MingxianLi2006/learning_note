x=linspace(0,2*pi,1000);
y1=0.2*exp(-0.5*x).*cos(4*pi*x);
y2=2*exp(-0.5*x).*cos(pi*x);
k=find(abs(y1-y2)<1e-2)

x1=x(k);
y3=0.2*exp(-0.5*x1).*cos(4*pi*x1);

plot(x,y1,x,y2,'k:',x1,y3,'bp');
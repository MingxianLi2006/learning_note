%lab assignment1
x=-5:1:5;           %范围
x1=double(x==0);    %x_1[n]=\delta[n]
x2=2*x1;            %x_2[n]=2*\delta[n]

figure(4)
y1=sin(pi/2*x1);
subplot(3,1,1);
stem(x,y1,'filled');
xlabel('n')
ylabel('sin(\delta[n])')

y2=sin(pi/2*x2);
subplot(3,1,2);
stem(x,y2,'filled')
xlabel('n')
ylabel('sin(2 \delta[n])')


y3=sin(pi/2*(x1+x2));
subplot(3,1,3);
stem(x,y1+y2,'r');
hold on;
stem(x,y3,'g');
legend('sin(\pi/2\cdot x1)+sin(\pi/2\cdot x2)','sin(pi/2\cdot(x1+x2))')
xlabel('n')
ylabel('output')

n=-5:9;
x1=double(n==0);
x2=2*double(n==0);
y1=sin(pi/2*x1);
y2=sin(pi/2*x2);
y_sum=sin(pi/2*(x1+x2));

figure;
subplot(3,1,1)
stem(n,y1,'filled');
title('y_1[n]:输入x_1[n]=\delta[n]');
xlabel('n');ylabel('y_1[n]');

subplot(3,1,2);
stem(n, y2, 'filled');
title('y_2[n]: 输入 x_2[n] = 2\delta[n]');
xlabel('n'); ylabel('y_2[n]');

subplot(3,1,3);
stem(n, y1 + y2, 'filled');
hold on;
stem(n, y_sum, 'r', 'filled');
title('蓝色: y_1[n]+y_2[n], 红色: 系统对 x_1+x_2 的实际输出');
xlabel('n'); ylabel('幅度');
legend('y_1+y_2', '实际输出');
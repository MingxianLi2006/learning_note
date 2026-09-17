x = -10:0.1:10;
y = x.^2;

disp(['numel(x) = ', num2str(numel(x))])
disp(['YScale = ', get(gca,'YScale')])
disp(['XScale = ', get(gca,'XScale')])

figure;
plot(x, y, 'o-')      % 加圆圈标记，看真实数据点
title('y = x^2')
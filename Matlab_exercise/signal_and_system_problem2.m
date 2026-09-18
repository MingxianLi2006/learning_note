% 输入定义在 -5 ≤ n ≤ 9
n_x = -5:9;
x = double(n_x >= 0);    % u[n]

% 输出定义在 -6 ≤ n ≤ 9
n_y = -6:9;

% 计算 y[n] = x[n] + x[n+1]
y = zeros(size(n_y));
for k = 1:length(n_y)
    n = n_y(k);
    % 取 x[n] 和 x[n+1] 的值，越界则视为 0
    xn = 0;
    xn1 = 0;
    if ismember(n, n_x),   xn  = x(n_x == n);   end
    if ismember(n+1, n_x), xn1 = x(n_x == n+1); end
    y(k) = xn + xn1;
end

% 画图
figure;
subplot(2,1,1);
stem(n_x, x, 'filled');
title('输入 x[n] = u[n]');
xlabel('n'); ylabel('x[n]');
xlim([-6 9]);

subplot(2,1,2);
stem(n_y, y, 'filled');
title('输出 y[n] = x[n] + x[n+1]');
xlabel('n'); ylabel('y[n]');
xlim([-6 9]);
%找函数零点
a=6;
b=10;
eps=1e-8%误差阈值
while 1
    c=(a+b)/2;
    fc=c^3-8*c^2+c-5;
    if abs(fc)<eps;
        break
    end
    fa=a^3-8*a^2+a-5;
    if fa*fc<0
        b=c;
    else
        a=c;
    end
end
x0=c;
x0
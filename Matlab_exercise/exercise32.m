% clc;
% clear;
% a=10+5*i;
% R=real(a)
% I=imag(a)
% M=abs(a)
% Angle=angle(a)
% A=magic(5)
% A([1 3],[2 3])
% b=input("hello")
% A=[1:1:b];
% sum(A)
A=[1 2;3,4];
triu(A)%A的上三角
tril(A)%A的下三角
flipud(A)%矩阵沿水平轴上下翻转
fliplr(A)%左右翻转
rot90(A)%逆时针旋转90度


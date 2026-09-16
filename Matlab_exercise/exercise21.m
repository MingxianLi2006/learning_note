%求当a取[0,2]上不同值的时候 e^x+x^a+x^(sqrt(x))=100的解
f=@(a)@(x)exp(x)+x^a+x^(sqrt(x))-100
%fzero
fzero(f(1),4);%4为初始值 从x0=4出发 找零点
A=0:0.1:2;
x=@(a)fzero(f(a),4)%x(a) 
X=@(A) arrayfun(@(a) x(a),A);%X(A)
Y=X(A)










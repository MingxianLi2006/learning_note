f=@(a)@(x)exp(x)+x^a+x^(sqrt(x))-100;
A=0:0.1:2;
x=@(a)fzero(f(a),4);
X=@(A)(arrayfun(x,A));
Y=X(A)
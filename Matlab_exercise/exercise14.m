A=randi([50,100],5,3);
any(A < 60,2);
all(A>=60,1);

%find 函数 k=fin(X) 返回一个包含数组X中每
% 个非零元素的线性索引的向量
% k=find(X,n,direction) direction可以为last 默认为first
B=randi([0,2],5,3)

ind=find(B>1)
ind2=find(B,2)%返回前两个非零值的索引
ind3=find(B,2,"last")%从后往前找
[row,col]=find(B);  %分别生成行列的列向量 非零值位置
[row,col,v]=find(B)%v 里面是所有的非零元素的值构成的列向量
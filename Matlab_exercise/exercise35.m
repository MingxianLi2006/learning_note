[A,B]=Mymatrix(5,6)
A
B

function [A,B]=Mymatrix(rownum,colnum)
for i=1:rownum
    for j=1:colnum
        A(i,j)=i+j;
        B(i,j)=i*j;
    end
end
end

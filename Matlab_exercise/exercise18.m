%function[输出形参表：output1...outputn]=函数名(输入形参表)
%函数体
%end

%调用函数
%[输出实参表]=函数名(输入实参表)
Y=1:20;
[maxVal,minVal]=max_min_values(Y);
maxVal
minVal

nums=input("input rownum and colnum:(eg.[2,5])");
myfun(nums(1),nums(2))
function[maxVal,minVal]=max_min_values(X)
maxVal=subfuc1(X);
minVal=subfuc2(X);
    function r=subfuc1(X)
        x1=sort(X,'descend');
        r=x1(1);
    end
    function r=subfuc2(X)
        x1=sort(X);
        r=x1(1);
    end
end


function A=myfun(rownum,colnum)
    for i=1:rownum
        for j=1:colnum
            A(i,j)=i+j;
        end
    end
end
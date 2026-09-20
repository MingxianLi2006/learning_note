%lab assignment2
n=[-10:1:10];
u1=(n>=0);
u2=(n>=-1);
y1=u1+u2;

figure(5)

subplot(3,1,1);
stem(n,u1);
xlim([-5 9]);
title("It's me")


subplot(3,1,2);
stem(n,u2);
xlim([-5 9])
xlabel("Input");
ylabel("x[n] and x[n+1]");
title('I love you')

subplot(3,1,3);
stem(n,y1,'r');
xlim([-6 9]);
xlabel("Output")
title('Hello')
sgtitle('what the fuck')
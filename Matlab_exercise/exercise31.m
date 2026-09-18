t=[0:0.001:1]
x=sin(2*pi*5*t);
noise=0.5*randn(size(t));
y=x+noise;
Y=fft(y); f=(0:length(Y)-1)*1000/length(Y);
plot(f,abs(Y));
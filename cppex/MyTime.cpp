#include<iostream>
#include<string>
class MyTime
{
	private:
		int hours;
		int minutes;
		int seconds;
	public:
		MyTime():hours(0),minutes(0),seconds(0){}
		MyTime(int h):minutes(0),seconds(0)
                {
                        hours=h;
                }
		MyTime(int h,int m):seconds(0)
		{
			minutes=m%60;
			hours=h+m/60;
		}
		MyTime(int h,int m,int s)
		{
			seconds=s;
			minutes=m;
			hours=h;

			minutes+=(seconds/60);
			hours+=minutes/60;

			minutes%=60;
			seconds%=60;
		}
		MyTime(const MyTime& other)
		{
			this->hours=other.hours;
			this->minutes=other.minutes;
			this->seconds=other.seconds;
		}
		MyTime operator+(const MyTime& t) const	//承诺不会改变成员变量
		{	//解决了sum=t1+t2的问题
			MyTime sum;
			sum.seconds=this->seconds+t.seconds;
			sum.minutes=this->minutes+t.minutes;
			sum.hours=this->hours+t.hours;

			sum.minutes+=sum.seconds/60;
			sum.hours+=sum.minutes/60;

			sum.minutes%=60;
			sum.seconds%=60;
			return sum;
		}
		MyTime operator+(int s) const
		{	//解决了t+m m为一个整数的问题
			MyTime sum;
			sum.seconds=this->seconds+s;
			sum.minutes=this->minutes+sum.seconds/60;
			sum.hours=this->hours+sum.minutes/60;

			sum.seconds%=60;
			sum.minutes%=60;

			return sum;
		}
		friend MyTime operator+(int m,const MyTime& t)
		{	//解决了m+t的问题
			return t+m;
		}
		MyTime& operator+=(const MyTime& t)	//引用传递
		{
			this->seconds+=t.seconds;
			this->minutes+=this->seconds/60;
			this->hours+=this->minutes/60;

			this->seconds%=60;
			this->minutes%=60;
			return *this;
		}
		friend std::ostream & operator<<(std::ostream & os, const MyTime& t)
		{
			std::string str=std::to_string(t.hours)+" hours and "+std::to_string(t.minutes)+" minutes and "+std::to_string(t.seconds)+" seconds.";
			os<<str;
			return os;

		}
		void printTime()
		{
			std::cout<<this->hours<<" hours "<<this->minutes<<" minutes "<<this->seconds<<" seconds ";
		}


};


int main()
{
	MyTime t4(1,50);
	MyTime t3(5);
	MyTime t1(1,80,270);
	MyTime t2(5,90,80);
	t1.printTime();
	std::cout<<"t1="<<t1<<std::endl;
	std::cout<<"t2="<<t2<<std::endl;
	MyTime sum=t1+t2;
	std::cout<<"sum=t1+t2="<<sum<<std::endl;
	t1+=t2;
	std::cout<<"Then after t1+=t2, t1="<<t1<<std::endl;
	t1=t1+50;
	std::cout<<"After t1=t1+50, t1="<<t1<<std::endl;
	t2=50+t2;
	std::cout<<"After t2=50+t2, t2="<<t2<<std::endl;
	return 0;
}

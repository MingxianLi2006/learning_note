#include<iostream>
#include<string>
using namespace std;
class Demo
{
	private:
		static size_t num;
		string name;
		int id;
	public:
		Demo()
		{
			num++;
		}
		Demo(string na_me,int i_d)
		{
			name=na_me;
			id=i_d;
			num++;
		}
		Demo(int i_d)
		{
			name=new char[1]{'\0'};
			id=i_d;
			num++;
		}
		~Demo()
		{
			num--;
		}
		static size_t getTotal(){return num;}


		void Display()
		{
			cout<<"this is: "<<this->name<<", id is: "<<this->id<<endl;
		}
		static void display()
		{
			cout<<"The value of the static num is: "<<num<<endl;
		}
};
size_t Demo::num=0;
int main()
{
	Demo obj;
	Demo obj1(1);

	obj.Display();
	obj1.Display();

	Demo::display();
	return 0;
}

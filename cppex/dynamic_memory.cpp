#include<iostream>
#include<cstring>
class Student
{
	private:
		char* name;
		double gpa;
		bool ismale;
	public:
		Student():name(new char[100]),gpa(0),ismale(true){std::cout<<"Use Constructor"<<std::endl;}
		Student(const char* na_me,double gp_a,bool is_male)
		{
			name=new char[100];
			strcpy(name,na_me);
			gpa=gp_a;
			ismale=is_male;
			std::cout<<"Use Constructor"<<std::endl;
		}
		~Student()
		{
			delete[] name;
			std::cout<<"Use Destructor"<<std::endl;
		}
		void printInfo()
		{
			std::cout<<" name = "<<name<<std::endl;
			std::cout<<" gpa ="<<gpa<<std::endl;
			std::cout<<" ismale "<<ismale<<std::endl;
		}

};
int main()
{
	Student class1[50]={Student("Li",3.89,1),Student("Tong",3.96,0),Student("Fang",1.50,1)};
	class1[0].printInfo();
	return 0;
}

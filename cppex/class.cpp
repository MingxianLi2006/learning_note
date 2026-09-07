#include<cstring>
#include <iostream>
using namespace std;
class Student
{
	private:
		char name[4];
		int born;
		bool male;
		int gpa;
	public:
		void setName(const char * s)
			{
				strncpy(name,s,sizeof(name));
			}
		void setBorn(int b)
			{
				born=b;
			}
		void setSex(bool isMale)
			{
				male=isMale;
			}
		void setGPA(int GPA)
			{
				gpa=GPA;
			}
		bool PrintInfo()
			{
				cout<<"Name: "<<name<<endl;
				cout<<"Born at: "<<born<<endl;
				cout<<"Ismale: "<<male<<endl;
				cout<<"GPA: "<<gpa<<endl;
				return true;
			}
};
int main()
{



	return 0;
}

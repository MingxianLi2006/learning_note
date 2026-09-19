#include<iostream>
#include<cstring>
using namespace std;
class Person
{
	
	public:
		string name;
		Person()
		{
			name="NULL";
		}
		Person(string n):name(n){}
		void print()
		{
			cout<<"Name: "<<name<<endl;
		}
};

class Student:public Person
{
	public:
		int id;
		Student(string Name,int ID)
		{
			name=Name;
			id=ID;
		}
		void print()
		{
			cout<<"Name: "<<name;
			cout<<".ID:"<<id<<endl;
		}

};
int main()
{
	Student yu("yu",1978);
	yu.print();
	Person *p=&yu;
	p->print();
	return 0;

}

#include<iostream>
enum DataType
{
	TYPE8U,
	TYPE8S,
	TYPE32F,
	TYPE64F
};
class Mat
{
	private:
		DataType type;
		void * data;
	public:
		Mat(DataType type):type(type),data(NULL){}
		DataType getType() const{return type;}
};
int main()
{
	Mat hello(TYPE8U);
	std::cout<<hello.getType()<<std::endl;
	return 0;
}

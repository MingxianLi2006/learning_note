#include<iostream>
class duck
{
    public:
        char* colour;
        int length;
        int weight;
    duck()
    {
        colour=new char[10]{"yellow"};
        length=0;
        weight=0;
    }
    ~duck()
    {
        delete[] colour;
    }
};

int main()
{



    return 0;
}
#include<iostream>
int main(int argc, char** argv) //get the order that user input in the terminal
{
    std::cout<<"The number of arguments is: "<<argc<<std::endl;
    std::cout<<"The name of program is: "<<argv[0]<<std::endl;
    std::string arg1=argv[1];
    if(arg1=="--help")
    {
        std::cout<<"here is program help, but the program is useless"<<std::endl;
    }
    return 0;
}
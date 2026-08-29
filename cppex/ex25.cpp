#include<iostream>
using namespace std;
int main()
{
	while (true)
	{
		char input_char;
		INPUT_CHAR:
		cin>>input_char;
		switch (input_char)
		{
        		case 'a':
        		case 'A':
                		cout<<"Move left"<<endl;
                		break;
        		case 'd':
        		case 'D':
                		cout<<"Move right"<<endl;
                		break;
			case 'q':
			case 'Q':
				cout<<"Game over"<<endl;
				return 0;
        		default:
                		cout<<"Undefined key."<<endl;
                		break;
		}
	}
	return 0;
}

#include <iostream>
#include<math.h>

using namespace std;

long long unsigned int ffact(long long unsigned int n)
{
	long long unsigned int o = 1;
	bool flag = 0;
	for (unsigned int i = 2; i <= n; i++)
	{
		for (int j = 7; j > 0; j--)
		{
//		cout << o << '-' << i << endl;
			if (i % (int)pow(5, j) == 0)
			{
//				cout << i << '-'<< j << endl;
				o = (o * i / (int)pow(10, j) )% 100000;
				flag = 1;
				break;
			}
		}	
		if (flag == 1)
		{
			flag = 0;
		}
		else
			o = o * i % 100000;
			
	}
//	cout << o << endl;}
	return o % 10;

}
int main()
{
	long long unsigned int n;
	cin >> n;
//	for (unsigned int i = 100; i <= n; i++)
//		cout << i << ": " << ffact(i) << endl;
	cout << ffact(n)  ;
    return 0;
}
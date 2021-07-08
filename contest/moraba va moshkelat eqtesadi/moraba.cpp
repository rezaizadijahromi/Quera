#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int n,k,s=0,c,j,sum;
	cin>>n;
	cin>>k;
	sum=n*k;
	
	for(int i=1;i<=n;i++)
	{
		cin>>c;
		if(c>=1&&c<=k)
		{
			s=s+c;
		}
	}
	
	sum=sum-s;
	
	j=sum/k;
	
	cout<<j;
}

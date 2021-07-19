#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>

using namespace std;

void maxTeams(){
    int a1, a2, a3;
    int b1, b2, b3;
    cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3;
    cout << min(a1, b1) + min(a2, b2) + min(a3, b3) << endl;
}

 
int main()
{
    maxTeams();
    
    return 0;
   
}

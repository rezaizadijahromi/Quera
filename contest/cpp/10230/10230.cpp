#include <iostream> 

using namespace std;

void  hamayesh(){
    int i, j, k;
    cin >> i >> j >> k;
    if (i >= 179 || j >= 179 || k >= 179 || i == 0 || j == 0 || k == 0)
    {
        cout << "No" << endl;
    }
    else if (i + j + k == 180)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}

int main()
{
    hamayesh();
    return 0;
}
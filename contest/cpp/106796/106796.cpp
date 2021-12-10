#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, k;
    string strArr;
    cin >> n >> k >> strArr;

    while (k--)
    {
        auto c = strArr[strArr.length() - 1];
        strArr.pop_back();
        strArr.insert(0, 1, c);

        for (auto &x : strArr)
        {
            
            if (x == 'z')
            {
                x = 'a';
            }
            else
            {
                x += 1;
            }
        }
    }

    cout << strArr << endl;

    return 0;
}
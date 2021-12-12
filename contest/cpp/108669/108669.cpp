#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

int main(){
   
    int n, firstExtra, secondExtra;
    cin >> n >> firstExtra >> secondExtra;
    vector<int> arr(n);

    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
    int split = -1;
    for (int i = 1; i < n; ++i)
    {
        if (arr[i - 1] > arr[i])
        {
            split = i - 1;
            break;
        }
    }

    if (split == -1)
    {
        cout << ((arr[n - 1] <= (90 + firstExtra)) ? "YES" : "NO") << endl;
    }
    else
    {
        if (arr[split] > (45 + firstExtra))
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << ((arr[n - 1] <= (90 + firstExtra)) ? "YES" : "NO") << endl;
        }
    }
}


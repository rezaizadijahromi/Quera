#include <iostream>
#include <vector>

using namespace std;

void heavy(){
    int n, m, count = 0;
    cin >> n >> m;
    vector<int> days(30, 0);
    
    n += m;
    while (n--)
    {
        int x, y;
        cin >> x >> y;
        for (int i = x; i <= y; ++i)
        {
            days[i - 1] += 1;
            if (days[i - 1] == 2)
            {
                ++count;
            }
        }
    }
    cout << count << endl;
}


int main(){

    heavy();
    return 0;
}

// g++ 3858.cpp -o 3858 && 3858
#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main(){
    int counter = 0;
    string s;

    cin >> s;
    for (auto c : s)
    {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        {
            ++ counter;
        }
    }

    cout << pow(2, counter);
}
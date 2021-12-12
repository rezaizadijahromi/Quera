#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    long q, l, r, c;
    cin >> q;

    while (q--)
    {
        c = 0;
        cin >> l >> r;

        long t = sqrtl(l);

        if (t * t < l)
        {
            ++t;
        }

        while (t * t <= r)
        {
            ++c;
            ++t;
        }

        cout << c << endl;
    }

    return 0;
}
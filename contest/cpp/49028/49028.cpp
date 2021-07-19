#include <iostream>
#include <vector>

void keyCount(){
    int n;
    std::cin >> n;
    int count = 0;
    int state = -1;
    while (n--)
    {
        int t;
        std::cin >> t;
        if (state == -1)
        {
            state = t;
        }
        else
        {
            if (state != t)
            {
                ++count;
                state = t;
            }
        }
    }
    std::cout << count << std::endl;

}

int main(){
    keyCount();

    return 0;
}
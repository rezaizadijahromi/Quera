#include <iostream>

int main(){
    int x, y;
    std::cin >> x >> y;

    std::cout << 1 << std::endl;

    if(x == 7 && y == 7){
        std::cout << 2 << " " << 2;
    }else{
        std::cout << 7 << " " << 7;
    }

    return 0;
}
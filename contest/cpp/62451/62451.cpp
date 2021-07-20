#include <iostream>

void torab(){
    int x1, v1, x2, v2;

    std::cin >> x1;
    std::cin >> v1;
    std::cin >> x2;
    std::cin >> v2;

    if(v1-v2 == 0){
        std::cout << "WAIT WAIT";
    }else{
        int vTeta = v1 - v2;
        int xTeta = x1 - x2;

        int a =  vTeta / xTeta;

        if(a < 0){
            std::cout << "SEE YOU";
        }else{
            std::cout << "BORO BORO";
        }
    }
}

int main(){
    torab();

    return 0;
}
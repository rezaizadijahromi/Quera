#include <iostream>

int month(int month, int day){
    int result = 0;
    if(month <= 6){
        result += 31 * (month - 1);
        result += day;
    }else if(month <= 31){
        result += (31 * 6) + ((month-7) * 30);
        result += day;
    }else{
        result = 365 - 29 + day;
    }

    return result;
}

void calculate(){
    int m1, d1, m2, d2;
    std::cin >> m1 >> d1 >> m2 >> d2;
    int i = month(m1, d1);
    int j = month(m2, d2);
    std::cout << ((i > j) ? (i - j) : (j - i)) << std::endl;
}

int main(){
    calculate();

    return 0;
}
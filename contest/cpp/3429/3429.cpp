#include <iostream>

using namespace std;

int main(){
    int degree;
    cin >> degree;

    if(degree > 100){
        cout << "Steam";
    }else if(degree < 0){
        cout << "Ice";
    }else{
        cout << "Water";
    }

    return 0;
}
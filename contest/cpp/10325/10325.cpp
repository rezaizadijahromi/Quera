#include <iostream>

using namespace std;

int main(){
    int r, c;
    cin >> r >> c;
    int a = 11 - r;
    string d;
    int s;

    if(c <= 10){
        d = "Right";
        s = c;    
    }else{
        d = "Left";
        s = 21 - c;
    }

    cout << d << " " << a << " " << s;

    return 0;
}



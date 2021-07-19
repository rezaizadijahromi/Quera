#include <iostream>

using namespace std;

void reDesign(){
    int x, y;
    cin >> x >> y;
    int r;
    cin >> r;
    int dx, dy;
    cin >> dx >> dy;

    if(x <= dx && dx <= x+r){
        if(dy >= y-r && dy <= y){
            cout << "Mahdi";
        }else{
            cout << "Parsa";
        }
    }else{
        cout << "Parsa";
    }


}

int main(){
    reDesign();

    return 0;
}
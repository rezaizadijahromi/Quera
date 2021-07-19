#include <iostream>

using namespace std;

void kaktoos(){
    int n, teams;

    cin >> n;

    for(int i=0; i < n; i++){
        cin >> teams;

        switch(teams){
            case 2:
                cout << "**" << endl;
                break;
            case 3:
                cout << "***"<< endl;
                break;
            default:
                cout << "*" << endl;
                break;
        }
    }
}

int main(){

    kaktoos();
    return 0;
}
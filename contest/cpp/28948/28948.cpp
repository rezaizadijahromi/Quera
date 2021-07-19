#include <iostream>
#include <algorithm>

using namespace std;


void bType(){
    string firstValue, lastValue;

    int back = 0;
    cin >> firstValue;
    reverse(firstValue.begin(), firstValue.end());

    for(int i=0; i < firstValue.length(); i++){
        if(firstValue[i] == '='){
            back++;
        }else if(back == 0){
            lastValue += firstValue[i];
        }else{
            back--;
        }
    }

    reverse(lastValue.begin(), lastValue.end());

    cout << lastValue << endl;
}

int main(){

    bType();

    return 0;
}
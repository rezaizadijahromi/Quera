#include <iostream>

using namespace std;

int main(){
    int n;

    cin >> n;

    int costumers;

    for(int i=2; i <= n; i++){
        if(n % i == 0){
            costumers = i;
            break;
        }
    }

    int result = n / costumers;

    cout << result;
}
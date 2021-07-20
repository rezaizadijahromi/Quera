#include <iostream>
#include <vector>

using namespace std;

void graph(){
    int n,k,m=0;
    cin >> n >> k;

    vector<int> arr;

    for(int i=0; i < n; i++){
        int j;
        cin >> j;
        arr.push_back(j);
    }

    int temp = 0;
    for(int i=0; i < arr.size(); i++){
        if(temp + arr[i] > k){
            m++;
            temp = arr[i];
        }else{
            temp += arr[i];
        }
    }

    cout << m + 1 << endl;

}

int main(){
    graph();

    return 0;
}
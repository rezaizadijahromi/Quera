#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void help(){
    int n;
    cin >> n;

    vector<int> lamps;
    vector<int> keys;
    vector<int> answers;

    int lamp, key;
    for(int i=0; i < n; i++){
        cin >> lamp;
        lamps.push_back(lamp);
    }

    for(int i=0; i < n; i++){
        cin >> key;
        keys.push_back(key);
    }

    for(int i=0; i < n; i++){
        if(keys[i] == 1){
            answers.push_back(lamps[i]);
        }
    }

    sort(answers.begin(), answers.end());

    for(int i=0; i < answers.size(); i++){
        cout << answers[i] << " ";
    }


}

int main(){
    help();

    return 0;
}
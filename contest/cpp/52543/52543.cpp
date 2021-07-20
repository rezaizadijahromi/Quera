#include <iostream>
#include <vector> 
#include <algorithm>

using namespace std;

void game(){
    int n;
    cin >> n;
    vector<int> list1;
    int input;
    for(int i=0; i < n; i++){
        cin >> input;
        list1.push_back(input);
    }

    sort(list1.begin(), list1.end());
     bool first = false;
    int i = 0, j = list1.size() - 1;

    while (n--)
    {
        cout << (first ? list1[i++] : list1[j--]) << " ";
        first = !first;
    }
    cout << endl;

    


}

int main(){
    game();

    return 0;
}
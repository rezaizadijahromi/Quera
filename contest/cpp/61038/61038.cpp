#include <iostream>
#include <vector>

using namespace std;

int gcd(int a,int b){
    if(b==0)return a;
    else return gcd(b,a%b);
}

void schoolDay(){
    vector<int> days;

    int n;
    int sequence;

    cin >> n;

    for(int i=0; i<n; i++){
        cin >> sequence;
        days.push_back(sequence);
    }

    int lcm = days[0];
    for(int i=1; i < days.size(); i++){
        lcm = (lcm * days[i]) / gcd(lcm, days[i]);
    }

    int javab = lcm % 30;
    cout << javab + 1 << endl;

}

int main(){

    schoolDay();

    return 0;
}
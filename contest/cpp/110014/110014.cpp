#include <iostream>
#include <string>

using namespace std;


int main(){
    char inp1, inp2, inp3, inp4;
    cin >> inp1 >> inp2 >> inp3 >> inp4;
    cout << (inp1 == inp2 || inp3 == inp4 || inp1 == inp4 || inp2 == inp3 ? "YES" : "NO") << endl;
    return 0;

}
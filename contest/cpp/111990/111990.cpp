#include <iostream>
#include <string>

using namespace std;


int main(){
    string banks [] = {"shanbe", "yekshanbe", "doshanbe", "seshanbe", "chaharshanbe", "panjshanbe"};

    string bank_name;

    cin >> bank_name;

    if(bank_name == "jome")
        cout << "tatil";
    else{
        for(int i=0; i <= 5; i++){
            if(bank_name == banks[i]){
                if(i % 2 == 0)
                    cout << "perspolis";
                else if(i % 2 == 1)
                    cout << "bahman";
            }
        }
    }


    return 0;
}
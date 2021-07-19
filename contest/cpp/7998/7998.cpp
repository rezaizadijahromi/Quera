#include <iostream>
#include <string>

void electionKey(){
    int n;

    std::cin >> n;
    std::string keys;

    std::string word;
    bool flag= false;

    for(int i=0; i<n; i++){
        std::cin >> keys;
        if(keys == "CAPS"){
            flag = !flag;
        }else if(flag){
            word += toupper(keys[0]);
        }else{
            word += keys[0];
        }
    }

    std::cout << word << std::endl;
}

int main(){
    electionKey();

    return 0;
}
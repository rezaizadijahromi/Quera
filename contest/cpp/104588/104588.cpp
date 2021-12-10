#include <iostream>

int main(){

   int counter = 0;
   int input;

   for(int i=0; i <= 4; i++){
       std::cin >> input;
       if(input >= 80)
            counter++;

   }

   if(counter >= 3)
        std::cout << "Mamma mia!" << std::endl;
   else if(counter == 1 || counter == 2)
        std::cout << "Mamma mia!!" << std::endl;
   else
        std::cout << "Mamma mia!!!" << std::endl;


    return 0;
}
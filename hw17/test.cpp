#include <typeinfo>
#include <iostream>
using namespace std;

class someClass { };

int main(int argc, char* argv[]) {
    
    int a = 0;
    // someClass b;
    // std::cout<<"a is of type: "<<typeid(a).name()<<std::endl; // Output 'a is of type int'
    // std::cout<<"b is of type: "<<typeid(b).name()<<std::endl; // Output 'b is of type someClass'
    a = 15;
    cout << a << endl; 
    return 0;
}
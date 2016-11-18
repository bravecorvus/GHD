#include <iostream>
using namespace std;

int main() {
    int userinput;
    bool looper = true;
    while (looper == true) {
        cout << "Enter a non-negative integer: ";
        cin >> userinput;
        if (userinput < 0) {
            cout << "Please enter a legitamate non-negative value" << endl;
        } else {
            float *thearray;
            thearray = new float[userinput];
            cout << "Enter 3 floating point values:\n";
            float temp;
            for(int i = 0; i < userinput; ++i) {
                cin >> temp;
                thearray[i] = temp;
            }
            cout << "In reverse order, your input is:" << endl;
            for(int i = userinput-1; i >= 0; --i) {
                cout << thearray[i] << endl;
            }
            break;
        }
    }
    
}
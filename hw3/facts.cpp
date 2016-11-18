/* print square roots in C++ language.  R. Brown, 9/2010 */

#include <iostream>
#include <cmath>
#include <string>

using namespace std;

long factorial(int input) {
  int facnum;
  int *intArray;
  if (input > 2) {
    facnum = input-1;
    intArray = new int[facnum];
    int counter = input;
    for(int x = 0; x < facnum; ++x) {
      intArray[x] = counter;
      counter -= 1;
    }
    long daReturn = 1;
    for(int x = 0; x < facnum; ++x) {
      daReturn *= intArray[x];
      // cout << daReturn << endl;
    }
    return daReturn;
  } else if (input == 2) {
    return 2;
  } else if (input == 1) {
    return 1;
  } else if (input == 0) {
    return 1;
  } else {
    cout << "Please enter a valid entry" << endl;
    return NULL;
  }
}

int main() {
  string userinput;
  while (true) {
    cout << "What number do you want the factorial of? (type 'exit' to exit)" << endl;
    cin >> userinput;
    if (userinput == "exit") {
      break;
    } else {
      int intuserinput = atoi(userinput.c_str());
      long dareturn = factorial(intuserinput);
      cout << "\nn--------------factorial(n)" << endl;
      cout << userinput << "                 "<< dareturn << endl;
    }
  }

  
  return 0;
}


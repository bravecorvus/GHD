/* print square roots in C++ language.  R. Brown, 9/2010 */

#include <iostream>
#include <cmath>
#include <string>

using namespace std;

long accumulatingvalue;

long factorial(int input, int acc) {
  int facnum;
  int *intArray;
  if (input > 2) {
    facnum = input-1;
    intArray = new int[facnum];
    int counter = input;
    int x = 0;
    while(x < facnum) {
      intArray[x] = counter;
      ++x;
      counter -=1;
    }
    // for(int x = 0; x < facnum; ++x) {
    //   intArray[x] = counter;
    //   counter -= 1;
    // }
    
    int z = 0;
    while(z < facnum) {
      acc *= intArray[z];
      ++z;
    }
  return acc;
  } else if (input == 2) {
    return 2;
  } else {
    return 1;
  }
}

int main() {
  string userinput;
  accumulatingvalue = 1;
  while (true) {
    cout << "What number do you want the factorial of? (type 'exit' to exit)" << endl;
    cin >> userinput;
    if (userinput == "exit") {
      break;
    } else {
      int intuserinput = atoi(userinput.c_str());
      long returnvalue = factorial(intuserinput, accumulatingvalue);
      cout << "\nn--------------factorial(n)" << endl;
      cout << userinput << "                 "<< returnvalue << endl;
    }
  }

  
  return 0;
}


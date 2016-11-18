#include <iostream>
using namespace std;

int main() {
  int n;
  int result = 0;  
  int i;

  cout << "Enter a positive integer: " << endl;
  cin >> n;

  // i = 0;
  // while (i <= n) {
  //   result = result + i*i; 
  //   i++;
  // }

  for(int i = 0; i <= n; ++i) {
    result = result + i*i;
  }

  printf("The sum of the first %d squares is %d.\n", n, result);
  return 0;  
}



// just to note, i never actually got 9 when i inputted -3
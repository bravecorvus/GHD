#include <iostream>
using namespace std;

int main() {
  int n;
  int result = 0;  
  int i;

  cout << "Enter a positive integer: " << endl;
  cin >> n;

  // printf("Enter a positive integer:  ");
  // scanf("%d", &n);

  i = 0;
  while (i <= n) {
    result = result + i*i; 
    i++;
  }

  printf("The sum of the first %d squares is %d.\n", n, result);
  return 0;  
}

#include <iostream>
using namespace std;

int arr[3];

int main() {
  arr[0] = 7;
  arr[1] = 3;
  arr[2] = 8;

  int x;
  x = 10;

  int *ip;
  ip = new int;
  *ip = 4;

  int *A;
  A = new int[6];
  A[3] = 99;
  A[4] = x;
  A[5] = *ip;

  int i;
  for (i = 0;  i < 3;  i++)
    A[i] = arr[i];

  for (i = 0;  i < 6;  i++)
    cout << A[i] << endl;

  delete ip;
  delete [] A;

  return 0;
}

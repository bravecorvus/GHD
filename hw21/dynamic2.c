#include <stdio.h>
#include <stdlib.h>

int arr[3];

int main() {
  arr[0] = 7;
  arr[1] = 3;
  arr[2] = 8;

  int x;
  x = 10;

  int *ip;
  ip = (int*) malloc(sizeof(int));
  *ip = 4;

  int *A;
  A = (int*) malloc(6*sizeof(int));
  A[3] = 99;
  A[4] = x;
  A[5] = *ip;

  int i;
  for (i = 0;  i < 3;  i++)
    A[i] = arr[i];

  for (i = 0;  i < 6;  i++)
    printf("%d\n", A[i]);

  free(ip);
  free(A);

  return 0;
}

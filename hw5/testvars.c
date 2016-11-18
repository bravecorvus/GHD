#include <stdio.h>

int n;   // global variable defined here
int addn(int x) {
  return x + n;
}
int main() {
  int val;
n = 7;
  printf("Enter an integer value:  ");
  scanf("%d", &val);
  printf("The call addn(%d) returns %d\n", val, addn(val));
}
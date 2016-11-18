

/* print square roots in C language.  R. Brown, 9/2010 */

#include <stdio.h>
#include <math.h>
/* print square roots in C++ language.  R. Brown, 9/2010 */

long factorial(int input) {
  int facnum;
  // int *intArray;
  if (input > 2) {
    facnum = input-1;
    int intArray[facnum];
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
  }
  return 1;
}

int main() {
  int userinput;
  while(1) {
    printf("What number do you want the factorial of? (type a negative number to exit)\n");
    scanf("%d",&userinput);
    if (userinput < 0) {
      break;
    } else {
      long dareturn = factorial(userinput);
      printf("\nn--------------factorial(n)\n");
      printf("%d", userinput);
      printf("          ");
      printf("%ld", dareturn);
      printf("\n");
    }
  }

  
  return 0;
}


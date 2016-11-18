

/* print square roots in C language.  R. Brown, 9/2010 */

#include <stdio.h>
#include <math.h>
/* print square roots in C++ language.  R. Brown, 9/2010 */


int userinput;
// userinput is out of the int main() {}
int facnum;
//facnum is outside of factorial();



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


void testingTheForLoop() {
  // Here is a test of a For loop, it will iterate 10 times from the initialization 0 ending at 9
  for(int i = 0; i < 10; ++i) {
    printf("The loop is in the ");
    printf("%d", i);
    printf(" iteration.\n");
  }
}

int main() {
  // Here is a while loop, it is initialized as true, and it broken by the action of the user entering a negative number
  while(1) {
    printf("What number do you want the factorial of? (type a 0 for the test for loop function, and type a negative number to exit)\n");
    scanf("%d",&userinput);
    if (userinput < 0) {
      break;
    } else if (userinput == 0) {
      testingTheForLoop();
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


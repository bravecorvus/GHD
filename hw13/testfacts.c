#include <stdio.h>

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n-1);
    }
}

int main() {
    int funcvalue;
    funcvalue = factorial(10);
    printf("%d", funcvalue);
}

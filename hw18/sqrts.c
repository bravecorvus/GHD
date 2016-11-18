#include <stdio.h>
#include <limits.h>  // for INT_MAX
#include <stdlib.h>  // for strtol
#include <math.h>


int main(int argc, char ** argv) {
    if(argc < 2) {
        printf("Terminating");
        return 0;
    } else {
        int x = strtol(argv[1], NULL, 10);
        printf("sqrt(n)\n--------\n");
        for (int n = 0; n < x; ++n) {
            printf("%lf", sqrt(n));
            printf("\n");
        }
    }
}
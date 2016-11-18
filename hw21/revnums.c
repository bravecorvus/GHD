#include <stdlib.h>
#include <stdbool.h>
int main() {
    int *N;
    N = (int*) malloc(sizeof(int));
    bool looper = true;
    while (looper == true) {
        printf("Enter a non-negative integer: \n");
        scanf("%d", N);
        printf("\n");
        if (*N < 0) {
            printf("Please enter a legitamate non-negative value\n");
        } else {
            float *A;
            A = (float*) malloc(*N*sizeof(float));
            printf("\n");
            printf("Enter 3 floating point values:\n");
            float *temp;
            temp = (float*) malloc(sizeof(float));
            for(int i = 0; i < *N; ++i) {
                scanf("%f", temp);
                A[i] = *temp;
            }
            printf("In reverse order, your input is:\n");
            for(int i = *N-1; i >= 0; --i) {
                printf("%f", A[i]);
                printf("\n");
            }
            break;
        }
    }
    
}
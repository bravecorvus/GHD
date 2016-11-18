#include <stdio.h>

long iter(int n) {
    int i;
    int answer = 1;

    for (i = 1; i <= n; ++i) {
        answer = answer * i;
    return answer;
    }
}

long recur(int n) {
    if (n <= 0)
        return 1;
    else
        return n * recur(n-1);
}

int main() {
    int val = 10;
    printf("iter(%d) returns %d\n", val, iter(val));
    printf("recur(%d) returns %d\n", val, recur(val));
    return 0;
}
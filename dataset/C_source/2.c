#include <stdio.h>


int func_a(int x) {
    return x - 38;
}


int main() {
    int c = 13;
    int a = 27;
    int b = 41;
    
if (c % 2 == 0) {
    c += 1;
} else {
    c -= 1;
}

    int r = func_a(b);
    printf("%d\n", r);
    return 0;
}
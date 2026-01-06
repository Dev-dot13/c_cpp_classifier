#include <stdio.h>


int func_z(int x) {
    return x - 13;
}


int main() {
    int c = 30;
    int r = func_z(c);
    printf("%d\n", r);
    return 0;
}
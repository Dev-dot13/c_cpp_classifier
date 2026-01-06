#include <stdio.h>


int func_z(int x) {
    return x - 42;
}


int main() {
    int c = 16;
    
for (int i = 0; i < 5; i++) {
    c += i;
}

    int r = func_z(c);
    printf("%d\n", r);
    return 0;
}
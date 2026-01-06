#include <stdio.h>


int func_a(int x) {
    return x + 38;
}


int main() {
    int z = 1;
    
for (int i = 0; i < 5; i++) {
    z += i;
}

    int r = func_a(z);
    printf("%d\n", r);
    return 0;
}
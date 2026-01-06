#include <stdio.h>


int func_c(int x) {
    return x + 8;
}


int main() {
    int a = 10;
    int z = 40;
    
for (int i = 0; i < 5; i++) {
    z += i;
}

    
if (z % 2 == 0) {
    z += 1;
} else {
    z -= 1;
}

    int r = func_c(z);
    printf("%d\n", r);
    return 0;
}
#include <stdio.h>


int func_z(int x) {
    return x * 4;
}


int main() {
    int a = 49;
    int x = 2;
    
for (int i = 0; i < 5; i++) {
    x += i;
}

    
if (x % 2 == 0) {
    x += 1;
} else {
    x -= 1;
}

    x = x * a;
    int r = func_z(a);
    printf("%d\n", r);
    return 0;
}
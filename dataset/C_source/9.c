#include <stdio.h>


int func_z(int x) {
    return x * 39;
}


int main() {
    int y = 15;
    int b = 33;
    
if (y % 2 == 0) {
    y += 1;
} else {
    y -= 1;
}

    
if (b % 2 == 0) {
    b += 1;
} else {
    b -= 1;
}

    y = y + b;
    
for (int i = 0; i < 5; i++) {
    y += i;
}

    
for (int i = 0; i < 5; i++) {
    b += i;
}

    int r = func_z(b);
    printf("%d\n", r);
    return 0;
}
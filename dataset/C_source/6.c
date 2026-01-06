#include <stdio.h>


int func_y(int x) {
    return x - 24;
}


int main() {
    int b = 34;
    int x = 40;
    int y = 38;
    
if (x % 2 == 0) {
    x += 1;
} else {
    x -= 1;
}

    
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

    b = b - y;
    int r = func_y(x);
    printf("%d\n", r);
    return 0;
}
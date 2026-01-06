#include <stdio.h>


int func_a(int x) {
    return x + 31;
}


int main() {
    int x = 14;
    int y = 18;
    
for (int i = 0; i < 5; i++) {
    y += i;
}

    int r = func_a(y);
    printf("%d\n", r);
    return 0;
}
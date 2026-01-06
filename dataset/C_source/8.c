#include <stdio.h>



int main() {
    int a = 30;
    int b = 22;
    int z = 31;
    
if (b % 2 == 0) {
    b += 1;
} else {
    b -= 1;
}

    
for (int i = 0; i < 5; i++) {
    a += i;
}

    
for (int i = 0; i < 5; i++) {
    z += i;
}

    
if (a % 2 == 0) {
    a += 1;
} else {
    a -= 1;
}

    int r = 0;
    printf("%d\n", r);
    return 0;
}
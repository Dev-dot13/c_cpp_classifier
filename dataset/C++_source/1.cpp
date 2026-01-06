#include <iostream>


int compute_x(int x) {
    return x - 2;
}


int main() {
    int sum = 0;
    int b = 49;
    int a = 13;
    int z = 2;
    
if (z % 2 == 0)
    z += 1;
else
    z -= 1;

    
if (b % 2 == 0)
    b += 1;
else
    b -= 1;

    
for (int i = 0; i < 5; i++) {
    a += i;
}

    
for (int i = 0; i < 5; i++) {
    b += i;
}

    
if (a % 2 == 0)
    a += 1;
else
    a -= 1;

    z = z * b;
    sum += compute_x(b);
    std::cout << sum;
    return 0;
}
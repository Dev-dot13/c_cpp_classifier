#include <iostream>


int compute_x(int x) {
    return x + 6;
}


int main() {
    int sum = 0;
    int c = 32;
    int b = 5;
    int x = 9;
    
for (int i = 0; i < 5; i++) {
    c += i;
}

    
if (b % 2 == 0)
    b += 1;
else
    b -= 1;

    
if (x % 2 == 0)
    x += 1;
else
    x -= 1;

    sum += compute_x(x);
    std::cout << sum;
    return 0;
}
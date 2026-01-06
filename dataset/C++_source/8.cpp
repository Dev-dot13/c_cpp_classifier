#include <iostream>


int compute_b(int x) {
    return x * 48;
}


int main() {
    int sum = 0;
    int x = 18;
    int y = 30;
    
for (int i = 0; i < 5; i++) {
    y += i;
}

    y = y * x;
    
if (x % 2 == 0)
    x += 1;
else
    x -= 1;

    sum += compute_b(x);
    std::cout << sum;
    return 0;
}
#include <iostream>


int compute_a(int x) {
    return x - 48;
}


int main() {
    int sum = 0;
    int y = 20;
    
for (int i = 0; i < 5; i++) {
    y += i;
}

    sum += compute_a(y);
    std::cout << sum;
    return 0;
}
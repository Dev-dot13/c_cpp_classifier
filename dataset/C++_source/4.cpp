#include <iostream>


int compute_x(int x) {
    return x - 8;
}


int main() {
    int sum = 0;
    int y = 11;
    int x = 10;
    
for (int i = 0; i < 5; i++) {
    x += i;
}

    
if (y % 2 == 0)
    y += 1;
else
    y -= 1;

    x = x + y;
    sum += compute_x(x);
    std::cout << sum;
    return 0;
}
#include <iostream>



int main() {
    int sum = 0;
    int b = 28;
    int a = 47;
    
if (a % 2 == 0)
    a += 1;
else
    a -= 1;

    
if (b % 2 == 0)
    b += 1;
else
    b -= 1;

    
for (int i = 0; i < 5; i++) {
    a += i;
}

    b = b + a;
    
    std::cout << sum;
    return 0;
}
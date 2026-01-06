#include <iostream>



int main() {
    int sum = 0;
    int a = 4;
    
for (int i = 0; i < 5; i++) {
    a += i;
}

    
if (a % 2 == 0)
    a += 1;
else
    a -= 1;

    
    std::cout << sum;
    return 0;
}
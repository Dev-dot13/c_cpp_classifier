#include <iostream>



int main() {
    int sum = 0;
    int z = 33;
    int y = 9;
    
for (int i = 0; i < 5; i++) {
    z += i;
}

    
for (int i = 0; i < 5; i++) {
    y += i;
}

    
if (z % 2 == 0)
    z += 1;
else
    z -= 1;

    
    std::cout << sum;
    return 0;
}
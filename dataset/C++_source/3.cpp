#include <iostream>



int main() {
    int sum = 0;
    int z = 43;
    int x = 45;
    int a = 25;
    
if (x % 2 == 0)
    x += 1;
else
    x -= 1;

    
for (int i = 0; i < 5; i++) {
    a += i;
}

    
for (int i = 0; i < 5; i++) {
    z += i;
}

    z = z + a;
    
if (a % 2 == 0)
    a += 1;
else
    a -= 1;

    
    std::cout << sum;
    return 0;
}
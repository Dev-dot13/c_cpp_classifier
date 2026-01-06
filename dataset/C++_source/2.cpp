#include <iostream>


int compute_c(int x) {
    return x * 43;
}


int main() {
    int sum = 0;
    int z = 17;
    int a = 50;
    
for (int i = 0; i < 5; i++) {
    a += i;
}

    
if (a % 2 == 0)
    a += 1;
else
    a -= 1;

    a = a + z;
    sum += compute_c(z);
    std::cout << sum;
    return 0;
}
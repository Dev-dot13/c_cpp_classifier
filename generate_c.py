import os
import random

def create_c_programs(output_dir, num_each_type=1):
    """Generate diverse C programs"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Type 1: Basic I/O
    for i in range(num_each_type):
        code = f'''#include <stdio.h>
#include <stdlib.h>

int main() {{
    int a = {random.randint(1, 100)};
    int b = {random.randint(1, 100)};
    printf("Result: %d\\n", a + b);
    return 0;
}}'''
        with open(f'{output_dir}/basic_io_{i}.c', 'w') as f:
            f.write(code)

    # Type 2: Array operations
    for i in range(num_each_type):
        code = f'''#include <stdio.h>

void process_array(int arr[], int size) {{
    int sum = 0;
    for(int i = 0; i < size; i++) {{
        sum += arr[i];
    }}
    printf("Array sum: %d\\n", sum);
}}

int main() {{
    int arr[5] = {{{random.randint(1, 10)}, {random.randint(1, 10)}, {random.randint(1, 10)}, {random.randint(1, 10)}, {random.randint(1, 10)}}};
    process_array(arr, 5);
    return 0;
}}'''
        with open(f'{output_dir}/array_ops_{i}.c', 'w') as f:
            f.write(code)

    # Type 3: File handling
    for i in range(num_each_type):
        code = f'''#include <stdio.h>

int main() {{
    FILE *file = fopen("temp_{i}.txt", "w");
    if(file) {{
        fprintf(file, "Test data %d\\n", {random.randint(100, 999)});
        fclose(file);
        printf("File created\\n");
    }}
    return 0;
}}'''
        with open(f'{output_dir}/file_handling_{i}.c', 'w') as f:
            f.write(code)

    # Type 4: String manipulation
    for i in range(num_each_type):
        code = f'''#include <stdio.h>
#include <string.h>

int main() {{
    char str1[50] = "Hello";
    char str2[] = "World";
    strcat(str1, " ");
    strcat(str1, str2);
    printf("Concatenated: %s\\n", str1);
    printf("Length: %lu\\n", strlen(str1));
    return 0;
}}'''
        with open(f'{output_dir}/string_manip_{i}.c', 'w') as f:
            f.write(code)

    # Type 5: Pointers
    for i in range(num_each_type):
        code = f'''#include <stdio.h>

void swap(int *a, int *b) {{
    int temp = *a;
    *a = *b;
    *b = temp;
}}

int main() {{
    int x = {random.randint(10, 50)};
    int y = {random.randint(10, 50)};
    printf("Before: x=%d, y=%d\\n", x, y);
    swap(&x, &y);
    printf("After: x=%d, y=%d\\n", x, y);
    return 0;
}}'''
        with open(f'{output_dir}/pointers_{i}.c', 'w') as f:
            f.write(code)

        # Type 6: Structures - FIXED
    for i in range(num_each_type):
        code = f'''#include <stdio.h>
#include <stdlib.h>  // Added for abs()

struct Point {{
    int x;
    int y;
}};

int main() {{
    struct Point p1 = {{.x = {random.randint(1, 100)}, .y = {random.randint(1, 100)}}};
    struct Point p2 = {{.x = {random.randint(1, 100)}, .y = {random.randint(1, 100)}}};
    printf("Distance: %d\\n", abs(p1.x - p2.x) + abs(p1.y - p2.y));
    return 0;
}}'''
        with open(f'{output_dir}/structures_{i}.c', 'w') as f:
            f.write(code)

    # Type 7: Dynamic memory
    for i in range(num_each_type):
        code = f'''#include <stdio.h>
#include <stdlib.h>

int main() {{
    int size = {random.randint(3, 8)};
    int *arr = (int*)malloc(size * sizeof(int));
    
    for(int i = 0; i < size; i++) {{
        arr[i] = i * {random.randint(2, 5)};
        printf("%d ", arr[i]);
    }}
    printf("\\n");
    
    free(arr);
    return 0;
}}'''
        with open(f'{output_dir}/dynamic_mem_{i}.c', 'w') as f:
            f.write(code)

    # Type 8: Recursion
    for i in range(num_each_type):
        code = f'''#include <stdio.h>

int factorial(int n) {{
    if(n <= 1) return 1;
    return n * factorial(n - 1);
}}

int main() {{
    int num = {random.randint(1, 10)};
    printf("Factorial of %d is %d\\n", num, factorial(num));
    return 0;
}}'''
        with open(f'{output_dir}/recursion_{i}.c', 'w') as f:
            f.write(code)

    # Type 9: Command line args
    for i in range(num_each_type):
        code = f'''#include <stdio.h>

int main(int argc, char *argv[]) {{
    printf("Program name: %s\\n", argv[0]);
    printf("Argument count: %d\\n", argc - 1);
    return 0;
}}'''
        with open(f'{output_dir}/cmd_args_{i}.c', 'w') as f:
            f.write(code)

    # Type 10: Math library
    for i in range(num_each_type):
        code = f'''#include <stdio.h>
#include <math.h>

int main() {{
    double angle = {random.uniform(0, 3.14)};
    printf("sin(%.2f) = %.3f\\n", angle, sin(angle));
    printf("cos(%.2f) = %.3f\\n", angle, cos(angle));
    printf("sqrt(%d) = %.3f\\n", {random.randint(2, 100)}, sqrt({random.randint(2, 100)}));
    return 0;
}}'''
        with open(f'{output_dir}/math_lib_{i}.c', 'w') as f:
            f.write(code)

if __name__ == '__main__':
    import sys
    num_each = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    create_c_programs('c_programs', num_each)
    print(f"Generated {num_each * 10} C programs")
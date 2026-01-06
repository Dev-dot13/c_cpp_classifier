import os
import random

def create_cpp_programs(output_dir, num_each_type=1):
    """Generate simple C++ programs that compile with default g++"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Type 1: Basic C++ with iostream
    for i in range(num_each_type):
        code = f'''#include <iostream>

int main() {{
    std::cout << "Hello C++ Program {i}" << std::endl;
    int x = {random.randint(1, 100)};
    int y = {random.randint(1, 100)};
    std::cout << "{random.randint(1, 100)} + {random.randint(1, 100)} = " << (x + y) << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/basic_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 2: Classes
    for i in range(num_each_type):
        code = f'''#include <iostream>

class Calculator {{
public:
    int add(int a, int b) {{ return a + b; }}
    int multiply(int a, int b) {{ return a * b; }}
}};

int main() {{
    Calculator calc;
    std::cout << "Add: " << calc.add({random.randint(1, 50)}, {random.randint(1, 50)}) << std::endl;
    std::cout << "Multiply: " << calc.multiply({random.randint(1, 20)}, {random.randint(1, 20)}) << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/class_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 3: Vectors
    for i in range(num_each_type):
        code = f'''#include <iostream>
#include <vector>

int main() {{
    std::vector<int> numbers;
    for(int j = 0; j < 5; j++) {{
        numbers.push_back(j * {random.randint(2, 10)});
    }}
    
    std::cout << "Vector contents: ";
    for(size_t j = 0; j < numbers.size(); j++) {{
        std::cout << numbers[j] << " ";
    }}
    std::cout << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/vector_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 4: References
    for i in range(num_each_type):
        code = f'''#include <iostream>

void increment(int& num) {{
    num++;
}}

int main() {{
    int value = {random.randint(1, 50)};
    std::cout << "Before: " << value << std::endl;
    increment(value);
    std::cout << "After: " << value << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/reference_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 5: Function overloading
    for i in range(num_each_type):
        code = f'''#include <iostream>

void print(int num) {{
    std::cout << "Integer: " << num << std::endl;
}}

void print(double num) {{
    std::cout << "Double: " << num << std::endl;
}}

void print(const char* text) {{
    std::cout << "String: " << text << std::endl;
}}

int main() {{
    print({random.randint(1, 100)});
    print({random.uniform(1.0, 10.0):.2f});
    print("C++ function overloading");
    return 0;
}}'''
        with open(f'{output_dir}/overload_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 6: Constructors/destructors
    for i in range(num_each_type):
        code = f'''#include <iostream>

class Test {{
public:
    Test() {{
        std::cout << "Constructor called" << std::endl;
        value = {random.randint(100, 200)};
    }}
    
    ~Test() {{
        std::cout << "Destructor called" << std::endl;
    }}
    
    int getValue() {{ return value; }}
    
private:
    int value;
}};

int main() {{
    Test obj;
    std::cout << "Value: " << obj.getValue() << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/ctor_dtor_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 7: Strings
    for i in range(num_each_type):
        code = f'''#include <iostream>
#include <string>

int main() {{
    std::string s1 = "Hello";
    std::string s2 = "World";
    std::string result = s1 + " " + s2;
    
    std::cout << result << std::endl;
    std::cout << "Length: " << result.length() << std::endl;
    std::cout << "First char: " << result[0] << std::endl;
    
    return 0;
}}'''
        with open(f'{output_dir}/string_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 8: Namespaces
    for i in range(num_each_type):
        code = f'''#include <iostream>

namespace Math {{
    int square(int x) {{ return x * x; }}
    int cube(int x) {{ return x * x * x; }}
}}

int main() {{
    int num = {random.randint(2, 10)};
    std::cout << num << " squared = " << Math::square(num) << std::endl;
    std::cout << num << " cubed = " << Math::cube(num) << std::endl;
    return 0;
}}'''
        with open(f'{output_dir}/namespace_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 9: Simple inheritance
    for i in range(num_each_type):
        code = f'''#include <iostream>

class Animal {{
public:
    virtual void speak() = 0;
}};

class Dog : public Animal {{
public:
    void speak() {{
        std::cout << "Woof!" << std::endl;
    }}
}};

class Cat : public Animal {{
public:
    void speak() {{
        std::cout << "Meow!" << std::endl;
    }}
}};

int main() {{
    Dog dog;
    Cat cat;
    
    dog.speak();
    cat.speak();
    
    return 0;
}}'''
        with open(f'{output_dir}/inherit_{i}.cpp', 'w') as f:
            f.write(code)
    
    # Type 10: Simple templates
    for i in range(num_each_type):
        code = f'''#include <iostream>

template<typename T>
T getMax(T a, T b) {{
    return (a > b) ? a : b;
}}

int main() {{
    std::cout << "Max of {random.randint(1, 50)} and {random.randint(1, 50)}: " 
              << getMax({random.randint(1, 50)}, {random.randint(1, 50)}) << std::endl;
    
    std::cout << "Max of {random.uniform(1.0, 10.0):.1f} and {random.uniform(1.0, 10.0):.1f}: " 
              << getMax({random.uniform(1.0, 10.0):.1f}, {random.uniform(1.0, 10.0):.1f}) << std::endl;
    
    return 0;
}}'''
        with open(f'{output_dir}/template_{i}.cpp', 'w') as f:
            f.write(code)

if __name__ == '__main__':
    import sys
    num_each = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    create_cpp_programs('cpp_programs', num_each)
    print(f"Generated {num_each * 10} C++ programs")
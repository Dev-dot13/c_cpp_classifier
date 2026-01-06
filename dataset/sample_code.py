import random

class SampleCodeGenerator:
    VARS = ["a", "b", "c", "x", "y", "z"]

    @staticmethod
    def _int():
        return random.randint(1, 50)

    @staticmethod
    def _op():
        return random.choice(["+", "-", "*"])

    # ----------------------------
    # C GENERATOR
    # ----------------------------
    @staticmethod
    def generate_c_codes(count=10):
        programs = []

        for _ in range(count):
            declared = []
            decl_stmts = []
            other_stmts = []

            # --- declare 1-3 variables first
            random.shuffle(SampleCodeGenerator.VARS)
            for v in SampleCodeGenerator.VARS[:random.randint(1, 3)]:
                declared.append(v)
                decl_stmts.append(f"int {v} = {SampleCodeGenerator._int()};")

            # --- arithmetic
            if len(declared) >= 2 and random.random() < 0.7:
                a, b = random.sample(declared, 2)
                other_stmts.append(f"{a} = {a} {SampleCodeGenerator._op()} {b};")

            # --- if statements
            for v in declared:
                if random.random() < 0.5:
                    other_stmts.append(f"""
if ({v} % 2 == 0) {{
    {v} += 1;
}} else {{
    {v} -= 1;
}}
""")

            # --- loops
            for v in declared:
                if random.random() < 0.5:
                    other_stmts.append(f"""
for (int i = 0; i < 5; i++) {{
    {v} += i;
}}
""")

            # --- optional function
            func_def = ""
            func_call = "int r = 0;"
            if random.random() < 0.7:
                fname = f"func_{random.choice(SampleCodeGenerator.VARS)}"
                arg = random.choice(declared)
                func_def = f"""
int {fname}(int x) {{
    return x {SampleCodeGenerator._op()} {SampleCodeGenerator._int()};
}}
"""
                func_call = f"int r = {fname}({arg});"

            random.shuffle(other_stmts)
            body = "\n    ".join(decl_stmts + other_stmts)

            code = f"""
#include <stdio.h>

{func_def}

int main() {{
    {body}
    {func_call}
    printf("%d\\n", r);
    return 0;
}}
"""
            programs.append(code.strip())

        return programs

    # ----------------------------
    # C++ GENERATOR
    # ----------------------------
    @staticmethod
    def generate_cpp_codes(count=10):
        programs = []

        for _ in range(count):
            declared = []
            decl_stmts = []
            other_stmts = []

            # --- declare 1-3 variables
            random.shuffle(SampleCodeGenerator.VARS)
            for v in SampleCodeGenerator.VARS[:random.randint(1,3)]:
                declared.append(v)
                decl_stmts.append(f"int {v} = {SampleCodeGenerator._int()};")

            # --- arithmetic
            if len(declared) >= 2 and random.random() < 0.7:
                a, b = random.sample(declared, 2)
                other_stmts.append(f"{a} = {a} {SampleCodeGenerator._op()} {b};")

            # --- if statements
            for v in declared:
                if random.random() < 0.5:
                    other_stmts.append(f"""
if ({v} % 2 == 0)
    {v} += 1;
else
    {v} -= 1;
""")

            # --- loops
            for v in declared:
                if random.random() < 0.5:
                    other_stmts.append(f"""
for (int i = 0; i < 5; i++) {{
    {v} += i;
}}
""")

            # --- optional function
            func_def = ""
            func_call = ""
            if random.random() < 0.7:
                fname = f"compute_{random.choice(SampleCodeGenerator.VARS)}"
                arg = random.choice(declared)
                func_def = f"""
int {fname}(int x) {{
    return x {SampleCodeGenerator._op()} {SampleCodeGenerator._int()};
}}
"""
                func_call = f"sum += {fname}({arg});"

            # --- sum variable for output
            sum_var = "sum"
            decl_stmts.insert(0, f"int {sum_var} = 0;")

            random.shuffle(other_stmts)
            body = "\n    ".join(decl_stmts + other_stmts)

            code = f"""
#include <iostream>

{func_def}

int main() {{
    {body}
    {func_call}
    std::cout << {sum_var};
    return 0;
}}
"""
            programs.append(code.strip())

        return programs

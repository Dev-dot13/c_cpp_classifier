import os
import subprocess
import glob

def compile_samples():
    # Compile C programs
    os.makedirs('samples/C', exist_ok=True)
    for c_file in glob.glob('c_programs/*.c'):
        base = os.path.splitext(os.path.basename(c_file))[0]
        output = f'samples/C/{base}.bin'
        subprocess.run(['gcc', '-o', output, c_file], check=False)
        print(f"Compiled: {c_file} -> {output}")
    
    # Compile C++ programs
    os.makedirs('samples/CPP', exist_ok=True)
    for cpp_file in glob.glob('cpp_programs/*.cpp'):
        base = os.path.splitext(os.path.basename(cpp_file))[0]
        output = f'samples/CPP/{base}.bin'
        subprocess.run(['g++', '-o', output, cpp_file], check=False)
        print(f"Compiled: {cpp_file} -> {output}")
    
    print(f"\nTotal binaries in samples/C: {len(os.listdir('samples/C'))}")
    print(f"Total binaries in samples/CPP: {len(os.listdir('samples/CPP'))}")

if __name__ == '__main__':
    compile_samples()
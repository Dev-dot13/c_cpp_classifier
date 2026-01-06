# dataset/dataset_generator.py
import subprocess
import os
import shutil

class DatasetGenerator:
    def __init__(self):
        self.c_compiler = 'gcc'
        self.cpp_compiler = 'g++'

        self.c_bin_dir = "./dataset/C"
        self.cpp_bin_dir = "./dataset/C++"
        self.c_source_dir = "./dataset/C_source"
        self.cpp_source_dir = "./dataset/C++_source"

        # Clear and recreate directories
        self._reset_dir(self.c_bin_dir)
        self._reset_dir(self.cpp_bin_dir)
        self._reset_dir(self.c_source_dir)
        self._reset_dir(self.cpp_source_dir)

    def _reset_dir(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)

    def generate_c_sample(self, source_code, index):
        samples = []

        source_path = os.path.join(self.c_source_dir, f"{index}.c")
        output_path = os.path.join(self.c_bin_dir, f"{index}.bin")

        with open(source_path, "w") as f:
            f.write(source_code)

        cmd = [self.c_compiler, '-o', output_path, source_path]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            samples.append({
                'path': output_path,
                'source_path': source_path,
                'language': 'C',
                'compiler': self.c_compiler,
                'index': index
            })
        except subprocess.CalledProcessError:
            pass

        return samples

    def generate_cpp_sample(self, source_code, index):
        samples = []

        source_path = os.path.join(self.cpp_source_dir, f"{index}.cpp")
        output_path = os.path.join(self.cpp_bin_dir, f"{index}.bin")

        with open(source_path, "w") as f:
            f.write(source_code)

        cmd = [self.cpp_compiler, '-o', output_path, source_path]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            samples.append({
                'path': output_path,
                'source_path': source_path,
                'language': 'C++',
                'compiler': self.cpp_compiler,
                'index': index
            })
        except subprocess.CalledProcessError:
            pass

        return samples

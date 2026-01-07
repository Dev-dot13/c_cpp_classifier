# create_dataset.py
from dataset.dataset_generator import DatasetGenerator
from dataset.sample_code import SampleCodeGenerator
from tqdm import tqdm
import os
import json
import sys

# ----------------------------
# Parse count argument
# ----------------------------
if len(sys.argv) != 2:
    print("Usage: python create_dataset.py <count>")
    sys.exit(1)

count = int(sys.argv[1])

# ----------------------------
# Prepare directories
# ----------------------------
os.makedirs("./dataset/C", exist_ok=True)
os.makedirs("./dataset/C++", exist_ok=True)

# ----------------------------
# Clear metadata.json explicitly
# ----------------------------
metadata_path = "./dataset/metadata.json"
with open(metadata_path, "w") as f:
    json.dump([], f)

# ----------------------------
# Generate dataset
# ----------------------------
dataset_gen = DatasetGenerator()
code_gen = SampleCodeGenerator()

metadata = []

# ----------------------------
# C samples
# ----------------------------
for i, code in tqdm(
    enumerate(code_gen.generate_c_codes(count)),
    total=count,
    desc="Generating C samples"
):
    metadata.extend(dataset_gen.generate_c_sample(code, i))

# ----------------------------
# C++ samples
# ----------------------------
for i, code in tqdm(
    enumerate(code_gen.generate_cpp_codes(count)),
    total=count,
    desc="Generating C++ samples"
):
    metadata.extend(dataset_gen.generate_cpp_sample(code, i))

# ----------------------------
# Save metadata
# ----------------------------
with open(metadata_path, "w") as f:
    json.dump(metadata, f, indent=2)

print(f"Dataset generated with {len(metadata)} binaries.")

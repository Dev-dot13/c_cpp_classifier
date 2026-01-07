# Binary Code Classification
This project classifies C vs C++ binaries using machine learning.

## Setup
1. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dataset
Generate sample binaries and metadata:
```bash
python create_dataset.py
```

## Train Model
Train the classifier and save the trained model:
```bash
python train.py
```

## Analyze Binary
Predict the language of a single binary:
```bash
python predict.py path/to/binary
```
Example:
```bash
python predict.py dataset/C/c_gcc_-O2_stripped.bin
```
Outputs probabilities for C and C++.

## Notes
1. Input to analyze must be a compiled binary, not source code.
2. To test with external binaries, provide the full path.
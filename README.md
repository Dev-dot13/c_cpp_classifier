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
python create_dataset.py <count>
```

## Train Model
Train the classifier and save the trained model:
```bash
python train_xgb2.py --samples-dir dataset --out model_bundle.joblib
```

## Analyze Binary
Predict the language of a single binary:
```bash
python predict_xgb2.py path/to/binary
```
Example:
```bash
python predict_xgb2.py tests/test1.bin
```
Outputs prediction for C and C++.

## Notes
1. Input to analyze must be a compiled binary, not source code.
2. To test with external binaries, provide the full path.

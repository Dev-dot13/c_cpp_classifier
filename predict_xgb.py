import pickle
import sys
import numpy as np
from feature_extractor import FeatureExtractor

def predict_binary(filepath):
    # Load model
    with open('model_xgb.pkl', 'rb') as f:
        data = pickle.load(f)
    
    model = data['model']
    extractor = FeatureExtractor()
    
    # Extract features
    features = extractor.extract(filepath)
    
    # Predict
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0]
    
    return "C++" if prediction == 1 else "C", prob

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python predict.py <binary_file>")
        sys.exit(1)
    
    result, probabilities = predict_binary(sys.argv[1])
    print(f"Prediction: {result}")
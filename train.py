import os
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from feature_extractor import FeatureExtractor

def collect_samples(samples_dir):
    X, y = [], []
    extractor = FeatureExtractor()
    
    # C binaries
    c_dir = os.path.join(samples_dir, 'C')
    if os.path.exists(c_dir):
        for file in os.listdir(c_dir):
            if file.endswith('.bin'):
                path = os.path.join(c_dir, file)
                features = extractor.extract(path)
                X.append(features)
                y.append(0)  # C label
    
    # C++ binaries
    cpp_dir = os.path.join(samples_dir, 'CPP')
    if os.path.exists(cpp_dir):
        for file in os.listdir(cpp_dir):
            if file.endswith('.bin'):
                path = os.path.join(cpp_dir, file)
                features = extractor.extract(path)
                X.append(features)
                y.append(1)  # C++ label
    
    return np.array(X), np.array(y)

def main():
    # Collect data
    X, y = collect_samples('samples')
    
    # Train model
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X, y)
    
    # Save model and extractor
    with open('model.pkl', 'wb') as f:
        pickle.dump({
            'model': model,
            'feature_names': FeatureExtractor().feature_names
        }, f)
    
    print(f"Model trained on {len(X)} samples")
    print(f"Accuracy: {model.score(X, y):.2%}")

if __name__ == '__main__':
    main()
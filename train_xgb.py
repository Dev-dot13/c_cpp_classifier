import os
import pickle
import numpy as np
from xgboost import XGBClassifier
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
    cpp_dir = os.path.join(samples_dir, 'C++')
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
    X, y = collect_samples('dataset')
    
    # Train model
    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X, y)
    
    # Save model and extractor
    with open('model_xgb.pkl', 'wb') as f:
        pickle.dump({
            'model': model,
            'feature_names': FeatureExtractor().feature_names
        }, f)
    
    print(f"Model trained on {len(X)} samples")
    print(f"Accuracy: {model.score(X, y):.2%}")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
train_xgb_classifier.py

Robust training script for distinguishing C vs C++ binaries using XGBoost.

Usage:
    python train_xgb_classifier.py --samples-dir dataset --out model_bundle.joblib
"""

import os
import argparse
import logging
import pickle
from collections import Counter

import numpy as np
import joblib
from tqdm import tqdm

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report, roc_auc_score
)
from xgboost import XGBClassifier

# Import your feature extractor (must provide .feature_names and .extract(path) -> array-like)
from feature_extractor import FeatureExtractor

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# -------------------------
# Helpers
# -------------------------
def collect_samples(samples_dir, extractor, verbose=True):
    """
    Collect features and labels from a dataset folder structured as:
      samples_dir/C/*.bin -> label 0
      samples_dir/C++/*.bin -> label 1

    Returns:
      X: 2D numpy array (n_samples, n_features)
      y: 1D numpy array (n_samples,)
      meta: list of (filepath, label)
    """
    X_list = []
    y_list = []
    meta = []

    expected_len = len(extractor.feature_names)

    # mapping: directory name -> label
    class_map = {'C': 0, 'C++': 1}

    for class_name, label in class_map.items():
        class_dir = os.path.join(samples_dir, class_name)
        if not os.path.isdir(class_dir):
            logger.warning("Class directory not found (skipping): %s", class_dir)
            continue

        files = [f for f in os.listdir(class_dir) if f.endswith('.bin')]
        if verbose:
            logger.info("Found %d .bin files in %s", len(files), class_dir)

        for fname in tqdm(files, desc=f"Processing {class_name}", disable=not verbose):
            path = os.path.join(class_dir, fname)
            try:
                features = extractor.extract(path)
                if features is None:
                    logger.warning("Extractor returned None for %s; skipping", path)
                    continue
                features = np.asarray(features, dtype=float)

                # Validate feature length
                if features.shape[0] != expected_len:
                    logger.warning(
                        "Feature length mismatch for %s: expected %d got %d. Skipping.",
                        path, expected_len, features.shape[0]
                    )
                    continue

                X_list.append(features)
                y_list.append(label)
                meta.append((path, label))
            except Exception as e:
                logger.exception("Failed to extract features from %s: %s", path, e)
                continue

    if len(X_list) == 0:
        raise RuntimeError("No valid samples collected. Check your dataset and FeatureExtractor.")

    X = np.vstack(X_list)
    y = np.array(y_list, dtype=int)
    logger.info("Collected %d samples across classes: %s", len(y), dict(Counter(y.tolist())))
    return X, y, meta

# -------------------------
# Main training function
# -------------------------
def train(
    samples_dir,
    output_path,
    test_size=0.2,
    random_state=42,
    use_cv=False,
    cv_folds=5,
    early_stopping_rounds=20,
    n_estimators=1000,
    n_jobs=4
):
    logger.info("Initializing FeatureExtractor")
    extractor = FeatureExtractor()

    logger.info("Collecting samples from %s", samples_dir)
    X, y, meta = collect_samples(samples_dir, extractor)

    # Basic label balance info
    counter = Counter(y.tolist())
    logger.info("Class distribution: %s", counter)

    # Stratified train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )
    logger.info("Train/test split: %d train, %d test", len(y_train), len(y_test))

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Handle class imbalance by computing scale_pos_weight for XGBoost (for binary)
    # scale_pos_weight should be (neg / pos)
    if len(counter) == 2:
        num_pos = counter.get(1, 0)
        num_neg = counter.get(0, 0)
        if num_pos == 0 or num_neg == 0:
            logger.warning("Only one class present in data; XGBoost may fail.")
            scale_pos_weight = 1.0
        else:
            scale_pos_weight = num_neg / num_pos
    else:
        # fallback
        scale_pos_weight = 1.0

    logger.info("Using scale_pos_weight=%s", scale_pos_weight)

    # Initialize XGBoost classifier
    model = XGBClassifier(
        n_estimators=n_estimators,
        max_depth=6,
        learning_rate=0.1,
        objective="binary:logistic",
        use_label_encoder=False,
        eval_metric="logloss",
        scale_pos_weight=scale_pos_weight,
        random_state=random_state,
        n_jobs=n_jobs
    )

    # Optional cross-validation before final training
    if use_cv:
        logger.info("Running Stratified %d-fold cross-validation", cv_folds)
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=skf, scoring='f1', n_jobs=n_jobs)
        logger.info("CV F1 scores: %s", np.round(cv_scores, 4))
        logger.info("CV F1 mean: %.4f ± %.4f", cv_scores.mean(), cv_scores.std())

    # Early stopping: hold out a small validation set from train
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train_scaled, y_train, test_size=0.15, stratify=y_train, random_state=random_state
    )
    logger.info("Using %d train / %d validation for early stopping", len(y_tr), len(y_val))

    logger.info("Fitting model with early stopping")
    model.fit(X_train_scaled, y_train)

    # Evaluate on test set
    logger.info("Evaluating on test set")
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else None

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    logger.info("Test Accuracy: %.4f", acc)
    logger.info("Test Precision: %.4f", prec)
    logger.info("Test Recall: %.4f", rec)
    logger.info("Test F1: %.4f", f1)
    logger.info("Confusion Matrix:\n%s", cm)
    logger.info("Classification Report:\n%s", classification_report(y_test, y_pred, digits=4))

    if y_prob is not None:
        try:
            roc = roc_auc_score(y_test, y_prob)
            logger.info("ROC-AUC: %.4f", roc)
        except Exception as e:
            logger.warning("Could not compute ROC-AUC: %s", e)

    # Feature importance (XGBoost's built-in)
    try:
        fi = model.get_booster().get_score(importance_type='gain')
        # convert to sorted list
        fi_items = sorted(fi.items(), key=lambda kv: kv[1], reverse=True)
        logger.info("Top feature importances (gain): %s", fi_items[:10])
    except Exception:
        logger.info("Could not extract feature importances from model.")

    # Save model bundle
    bundle = {
        'model': model,
        'scaler': scaler,
        'feature_names': extractor.feature_names,
        'meta': {
            'samples_dir': samples_dir,
            'class_map': {'C': 0, 'C++': 1},
            'random_state': random_state,
            'test_size': test_size,
            'n_estimators': n_estimators
        }
    }
    joblib.dump(bundle, output_path)
    logger.info("Saved model bundle to %s", output_path)


# -------------------------
# CLI
# -------------------------
def parse_args():
    p = argparse.ArgumentParser(description="Train XGBoost classifier for C vs C++ binaries")
    p.add_argument("--samples-dir", type=str, required=True, help="Path to dataset folder (contains C/ and C++/)")
    p.add_argument("--out", type=str, default="model_bundle.joblib", help="Path to save model bundle")
    p.add_argument("--test-size", type=float, default=0.2, help="Test set fraction")
    p.add_argument("--random-state", type=int, default=42)
    p.add_argument("--use-cv", action="store_true", help="Run cross-validation before training")
    p.add_argument("--cv-folds", type=int, default=5, help="Number of CV folds")
    p.add_argument("--n-jobs", type=int, default=4, help="Number of parallel jobs")
    p.add_argument("--n-estimators", type=int, default=1000, help="Maximum number of boosting rounds (XGBoost)")
    p.add_argument("--early-stopping", type=int, default=20, help="Early stopping rounds")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    try:
        train(
            samples_dir=args.samples_dir,
            output_path=args.out,
            test_size=args.test_size,
            random_state=args.random_state,
            use_cv=args.use_cv,
            cv_folds=args.cv_folds,
            early_stopping_rounds=args.early_stopping,
            n_estimators=args.n_estimators,
            n_jobs=args.n_jobs
        )
    except Exception as e:
        logger.exception("Training failed: %s", e)
        raise

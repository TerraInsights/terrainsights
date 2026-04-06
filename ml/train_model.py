import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

def train():
    print("Loading data...")
    # Path to the dataset
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fertilizer_recommendation.csv')
    df = pd.read_csv(data_path)
    
    print("Dataset shape:", df.shape)
    
    target = 'Recommended_Fertilizer'
    X = df.drop(columns=[target])
    y = df[target]
    
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    print(f"Categorical features ({len(categorical_cols)}):", categorical_cols)
    print(f"Numeric features ({len(numeric_cols)}):", numeric_cols)
    
    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ])
    
    # Model pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42))
    ])
    
    print("Training model...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"Model accuracy on test set: {score:.4f}")
    
    # Save the model
    model_out = os.path.join(os.path.dirname(__file__), 'fertilizer_model.pkl')
    joblib.dump(model, model_out)
    print(f"Model saved to {model_out}")

if __name__ == "__main__":
    train()

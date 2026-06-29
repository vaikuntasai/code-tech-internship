# task1_data_pipeline.py

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def run_pipeline():
    print("--- Starting Task 1: Data Pipeline ---")
    
    # 1. EXTRACT: Create mock data with missing values
    data = {
        'Age': [25, np.nan, 30, 45, 22],
        'Salary': [50000, 60000, 55000, np.nan, 48000],
        'City': ['NY', 'LA', 'NY', np.nan, 'LA']
    }
    df = pd.DataFrame(data)
    print("Original Data:\n", df, "\n")

    # 2. TRANSFORM: Define the preprocessing steps
    numeric_features = ['Age', 'Salary']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')), 
        ('scaler', StandardScaler())                 
    ])

    categorical_features = ['City']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')), 
        ('onehot', OneHotEncoder(handle_unknown='ignore'))    
    ])

    # Combine transformers
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 3. LOAD: Execute pipeline
    processed_data = preprocessor.fit_transform(df)

    print("Processed Data Array:\n", processed_data)
    print("--- ETL Pipeline Executed Successfully! ---\n")

if __name__ == "__main__":
    run_pipeline()

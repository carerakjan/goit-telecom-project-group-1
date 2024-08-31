import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

def processing_data(file_csv):
    df = pd.read_csv(file_csv)
    df = df.drop(columns=['id'])
    df = df.astype(float)
    missing_values = df.isnull().sum() / len(df)
    columns_to_drop = [column for column in df.columns if missing_values[column] > 0.5]
    df_cleaned = df.drop(columns=columns_to_drop)
    df_cleaned = df_cleaned.dropna(subset=['download_avg', 'upload_avg'])
    if 'reamining_contract' in df_cleaned.columns:
        df_cleaned.loc[:, 'reamining_contract'] = df_cleaned['reamining_contract'].fillna(0)
    columns_to_remove = ['bill_avg', 'service_failure_count']
    df_cleaned = df_cleaned.drop(columns=[col for col in columns_to_remove if col in df_cleaned.columns])
    scaler = StandardScaler()
    numerical_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    df_cleaned[numerical_columns] = scaler.fit_transform(df_cleaned[numerical_columns])   
    df_cleaned.to_csv('internet_service_churn_updated.csv', index=False)
    return df_cleaned

# processed_df = processing_data('project/data/internet_service_churn.csv')

def processing_input_data(input_data):
    # Создаем DataFrame
    df = pd.DataFrame([input_data])
    print("Original DataFrame:")
    print(df)
    
    with open('project/data/scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)

    numerical_features = ["is_tv_subscriber","is_movie_package_subscriber","subscription_age","reamining_contract","download_avg","upload_avg","download_over_limit"]



    df[numerical_features] = scaler.transform(df[numerical_features])
    print(df.head())
    return df


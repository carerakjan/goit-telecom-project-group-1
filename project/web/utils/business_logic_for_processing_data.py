import pickle
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
import shap
import lime.lime_tabular
import pickle

import lime.lime_tabular  # Для LIME
import pandas as pd
import joblib  # Для збереження та завантаження моделі
import os
from web.utils.function_for_processing import processing_input_data

 

# Завантаження моделі
model_path = 'project/models/decision_tree.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


def visualize_churn_categories(data):
    churn_counts = data['churn_category'].value_counts()
    
    # Створюємо графік
    fig, ax = plt.subplots(figsize=(6, 4))  # Задайте тут бажані розміри фігури
    wedges, texts, autotexts = ax.pie(
        churn_counts,
        labels=churn_counts.index,
        autopct=lambda pct: func(pct, churn_counts),
        startangle=70
    )
    
    # Налаштування стилю підписів
    for text in texts:
        text.set(size=7)
    for autotext in autotexts:
        autotext.set(size=7, weight='bold')
    
    # Відображення графіка безпосередньо у веб-додатку
    st.pyplot(fig)

def make_predictions(data):
    try:
        # Перевірка наявності ідентифікаторного стовпця
        if 'id' in data.columns:
            id_column = 'id'
        elif 'last_name' in data.columns:
            id_column = 'last_name'
        else:
            return None, ['Не вдається визначити ідентифікаторний стовпець.']

        # Вилучення відсутніх колонок, які не використовувалися під час навчання
        columns_for_prediction = data.drop(columns=['bill_avg', 'service_failure_count', id_column], errors='ignore')

        # Виконання передбачень
        predictions = model.predict_proba(columns_for_prediction)[:, 1]

        # Додавання результатів передбачень до вихідних даних
        data['churn_probability'] = predictions
        data['churn_category'] = ['висока' if p > 0.5 else 'низька' for p in predictions]

        return filter_columns(data), None
    except Exception as e:
        return None, [str(e)]

def func(pct, allvals):
    absolute = int(pct / 100. * sum(allvals))
    return f'{absolute} з {sum(allvals)} ({pct:.1f}%)'

def filter_columns(data):
    # Стовпці, які потрібно залишити
    columns_to_keep = ['churn_category', 'churn_probability', 'id']
    
    # Перевірте, чи є ці стовпці в DataFrame
    existing_columns = [col for col in columns_to_keep if col in data.columns]
    
    # Вилучіть усі стовпці, які не входять до списку 'existing_columns'
    filtered_data = data[existing_columns]
    
    return filtered_data


def predict_single_user(data):
    # Завантаження моделі
    model_path = 'project/models/decision_tree.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
        
    try:
        # Обробка вхідних даних і забезпечення правильного порядку стовпців
        input_data = processing_input_data(data)
        
        # Вказаний порядок ознак, який очікується моделлю
        model_feature_order = ['is_tv_subscriber', 'is_movie_package_subscriber', 'subscription_age',
                               'reamining_contract', 'download_avg', 'upload_avg', 'download_over_limit']
        
        # Переконайтеся, що input_data має той самий порядок стовпців, що і model_feature_order
        input_data = input_data[model_feature_order]
        
        # Прогнозування ймовірностей
        predictions = model.predict_proba(input_data)[:, 1]
        
        # Виведення ймовірностей
        print(f"Ймовірності прогнозування: {predictions}")
        
        # Встановлення ймовірності відтоку та категорії
        input_data['churn_probability'] = predictions
        input_data['churn_category'] = ['висока' if p > 0.5 else 'низька' for p in predictions]
        
        return filter_columns(input_data)
    
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return pd.DataFrame()
   
       
           
       
   



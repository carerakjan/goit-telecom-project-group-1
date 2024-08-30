import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Завантаження моделі
model_path = 'project/models/decision_tree.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Завантаження даних для отримання імен ознак
data_path = 'project/data/internet_service_churn_scaled.csv'
dataFile = pd.read_csv(data_path)

def plot_feature_importance(feature_names, importances):
    sorted_idx = np.argsort(importances)
    
    plt.figure(figsize=(6, 4))
    plt.barh(np.array(feature_names)[sorted_idx], importances[sorted_idx])
    plt.xlabel("Важливість ознак")
    plt.ylabel("Ознаки")
    plt.title("Важливість ознак в Decision Tree")
    
    # Відображення графіка безпосередньо у веб-додатку
    st.pyplot(plt)

def display_feature_importance():
    if hasattr(model, 'feature_importances_'):
        feature_names = dataFile.columns.tolist()  # Отримання імен ознак з даних
        importances = model.feature_importances_
        plot_feature_importance(feature_names, importances)
    else:
        st.error("Модель не підтримує оцінку важливості ознак.")

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
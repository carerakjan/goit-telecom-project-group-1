import joblib  # Для завантаження моделі
import numpy as np  # Для обробки масивів даних
import matplotlib.pyplot as plt  # Для побудови графіків
import streamlit as st  # Для відображення графіків у Streamlit
import shap  # Для пояснення моделей за допомогою SHAP
import os
from sklearn.utils import shuffle
from web.utils.get_main_features import get_feature_titles
from web.utils.load_mertics import load_metrics
from web.utils.load_model import get_model

def load_importances(file_path):
    return joblib.load(file_path)

def get_metrics_by_model(model_name: str):
    model_name = model_name.split(".")[0]  # Видалення розширення файлу з назви моделі
    metrics = dict(load_metrics())  # Завантаження метрик
    precision, thresholds, current_threshold = metrics[
        model_name
    ]  # Отримання метрик для моделі
    return precision, thresholds, current_threshold


@st.cache_data
def models_bar_plot(model_name):
  
    data = load_metrics()  # Завантаження метрик
    precision, recall, _ = get_metrics_by_model(model_name)

    # Виділяємо одну з моделей
    highlight_model = model_name.split(".")[0]

    # Збираємо дані для графіка
    models = [item[0] for item in data]  # Назви моделей
    second_elements = [item[1][1][1] for item in data]  # Точність моделей
    highlight_color = "orange"  # Колір для виділеної моделі
    default_color = "blue"  # Колір для інших моделей

    # Створюємо список кольорів для кожного стовпця
    colors = [
        highlight_color if model == highlight_model else default_color
        for model in models
    ]

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    bars = plt.bar(models, second_elements, color=colors)

    # Додаємо підписи і заголовки
    plt.xlabel("Модель")
    plt.ylabel("Точність")
    plt.title(
        f"Дана модель серед інших - точнсть: {precision[1]:.2f} при повноті: {recall[1]:.2f}"
    )

    # Повертаємо розмітку
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # Відповідне розташування елементів
    plt.grid()  # Додаємо сітку для зручності

    # Відображення графіка у Streamlit
    st.pyplot(plt)



def plot_feature_importance(importances, feature_names, title):
    plt.figure(figsize=(10, 6))
    
    # Отображение горизонтального бар-графика
    plt.barh(
        np.array(feature_names),  # Список имен признаков
        importances,  # Важность признаков
        color="skyblue",
    )
    
    # Установка меток оси X и пределов
    plt.xlabel("Важливість")
    plt.ylabel("Особливості")
    plt.title(title)
    plt.gca().invert_yaxis()  # Перевертання осі Y для відображення найбільш важливих ознак вгорі

    # Установка пределов и меток оси X
    plt.xlim(0, 1)  # Установка диапазона оси X от 0 до 2
    plt.xticks(np.arange(0, 1.1, 0.1))  # Установка меток с шагом 0.2

    # Отображение графика в Streamlit
    st.pyplot(plt)
    
    # Очистка текущего графика, чтобы предотвратить наложение при многократных вызовах функции
    plt.clf()

def plot_model_importance(model_name, file_path, X, feature_names, plot_title):
    importances = load_importances(file_path)
    
    if importances is not None:
        # Перевірка типу даних
        if "svm" in model_name and importances is not None:
            importances = importances.abs()  # Для SVM можливо варто взяти абсолютні значення
        
        if "logistic_regression" in model_name and importances is not None:
            importances = importances.abs()  # Для SVM можливо варто взяти абсолютні значення
        plot_feature_importance(importances, feature_names, plot_title)
        models_bar_plot(model_name)

def select_plot(model_name, X, feature_names):
    model_functions = {
        "logistic_regression_model.pkl": "logistic_regression_model_importances.pkl",
        "decision_tree.pkl": "decision_tree_importances.pkl",
        "svm_model_linear.pkl": "svm_importances_linear.pkl",
        "svm_model_poly.pkl": "svm_importances_poly.pkl",
        "svm_model_rbf.pkl": "svm_importances_rbf.pkl",
        "neural_model_MLP.pkl": "neural_model_MLP_importances.pkl",
        "svm_model_sigmoid.pkl": "svm_importances_sigmoid.pkl",
    }

    plot_titles = {
        "logistic_regression_model.pkl": "Важливість ознак - Логістична регресія",
        "decision_tree.pkl": "Важливість ознак - Дерево рішень",
        "svm_model_linear.pkl": "Важливість ознак - Лінійний SVM",
        "svm_model_poly.pkl": "Важливість ознак - Поліноміальний SVM",
        "svm_model_rbf.pkl": "Важливість ознак - RBF SVM",
        "neural_model_MLP.pkl": "Важливість ознак - Логістична нейромережі",
        "svm_model_sigmoid.pkl": "Важливість ознак - SVM Sigmoid",
    }

    directory_path = "project/models/importances_models/"
    
    if model_name not in model_functions:
        st.error("Невірне ім'я моделі.")
        return

    file_name = model_functions[model_name]
    file_path = directory_path + file_name
    plot_title = plot_titles[model_name]

    plot_model_importance(model_name, file_path, X, feature_names, plot_title)

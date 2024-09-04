import numpy as np  # Для обробки масивів даних
import matplotlib.pyplot as plt  # Для побудови графіків
import streamlit as st  # Для відображення графіків у Streamlit
import joblib  # Для збереження та завантаження моделі
import os  # Для роботи з файловою системою
import pandas as pd  # Для роботи з даними у форматі DataFrame
from web.utils.function_for_processing import processing_input_data
from web.utils.scale_data import scale, prepare_data
from web.utils.load_model import get_model, get_model_name
from web.utils.predict_by_model import get_predict
from collections import defaultdict


def visualize_churn_categories(data):
    churn_counts = data["Категорія відтоку"].value_counts()

    print("churn_counts:visualize_churn_categories>>>>", churn_counts)

    # Створюємо графік
    fig, ax = plt.subplots(figsize=(6, 4))  # Задайте тут бажані розміри фігури
    wedges, texts, autotexts = ax.pie(
        churn_counts,
        labels=churn_counts.index,
        autopct=lambda pct: func(pct, churn_counts),
        startangle=70,
    )

    # Налаштування стилю підписів
    for text in texts:
        text.set(size=7)
    for autotext in autotexts:
        autotext.set(size=7, weight="bold")

    # Відображення графіка безпосередньо у веб-додатку
    st.pyplot(fig)


def visualize_churn_categories_bar(data):
    # Список всіх моделей
    all_models = [
        "decision_tree.pkl",
        "logistic_regression_model.pkl",
        "svm_model_linear.pkl",
        "neural_model_MLP.pkl",
        "svm_model_sigmoid.pkl",
        "svm_model_poly.pkl",
        "svm_model_rbf.pkl"
    ]
    
    # Створюємо DataFrame з нульовими значеннями для всіх можливих моделей та категорій
    categories = ["висока", "середня", "низька"]
    model_category_counts = pd.DataFrame(index=all_models, columns=categories).fillna(0)
    
    # Підрахунок кількості записів для кожної категорії відтоку в межах кожної моделі
    for model in all_models:
        for category in categories:
            model_category_counts.loc[model, category] = data[(data["Модель"] == model) & (data["Категорія відтоку"] == category)].shape[0]
    
    # Створюємо графік
    fig, ax = plt.subplots(figsize=(14, 6))  # Зменшено значення висоти графіка

    # Кольори для категорій
    colors = {
        "висока": "red",
        "середня": "yellow",
        "низька": "green"
    }
    
    # Ширина стовпчиків
    bar_width = 0.3
    
    # Побудова стовпчиків
    for i, model in enumerate(all_models):
        counts = model_category_counts.loc[model]
        total = counts.sum()
        if total == 0:  # Якщо немає записів для моделі, пропускаємо побудову
            continue
        bottom = 0
        for category in categories:
            category_count = counts[category]
            percentage = (category_count / total) * 100 if total > 0 else 0
            # Малюємо стовпчики
            bar = ax.bar(
                i,
                category_count,
                width=bar_width,
                bottom=bottom,
                color=colors[category],
                label=category if i == 0 else "",
                edgecolor='black'
            )
            # Додаємо текст із відсотками
            if category_count > 0:  # Текст тільки для категорій, де є дані
                ax.text(
                    i,
                    bottom + category_count * 0.5,  # Піднімаємо текст для середини стовпчика
                    f'{percentage:.1f}%',
                    ha='center',
                    va='center',
                    color='black',
                    fontsize=9
                )
            bottom += category_count
    
    # Налаштування підписів та заголовків
    ax.set_xlabel('Модель')
    ax.set_ylabel('Кількість записів')
    ax.set_title('Розподіл категорій відтоку для кожної моделі')
    
    # Додаємо легенду
    handles = [plt.Rectangle((0,0),1,1, color=colors[cat]) for cat in categories]
    ax.legend(handles, categories, title="Категорія відтоку")
    
    # Налаштування підписів осі X
    ax.set_xticks(range(len(all_models)))
    ax.set_xticklabels(all_models, rotation=45, ha="right")

    # Відображення графіка безпосередньо у веб-додатку
    st.pyplot(fig)



def probability_to_text(probabilities):
    return [
        "висока" if p >= 0.75 else "середня" if 0.5 <= p < 0.75 else "низька"
        for p in probabilities
    ]


def make_predictions(data):
    try:
        if "id" in data.columns:
            id_column = "id"
            output = pd.DataFrame(data[id_column])
        else:
            output = pd.DataFrame()
        predictions = get_predict(data)
        # Додавання результатів передбачень до вихідних даних
        output["Категорія відтоку"] = probability_to_text(predictions)
        output["Вірогідність відтоку"] = predictions
        output["Модель"] = st.session_state.selected_model
        print(">>", output)

        return output, None
    except Exception as e:
        return None, [str(e)]


def func(pct, allvals):
    absolute = int(pct / 100.0 * sum(allvals))
    return f"{absolute} з {sum(allvals)} ({pct:.1f}%)"

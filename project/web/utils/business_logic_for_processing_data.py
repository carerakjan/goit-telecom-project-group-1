import numpy as np  # Для обробки масивів даних
import matplotlib.pyplot as plt  # Для побудови графіків
import streamlit as st  # Для відображення графіків у Streamlit
import joblib  # Для збереження та завантаження моделі
import os  # Для роботи з файловою системою
import pandas as pd  # Для роботи з даними у форматі DataFrame
from web.utils.function_for_processing import processing_input_data
from web.utils.scale_data import scale,prepare_data
from web.utils.load_model import get_model, get_model_name





def visualize_churn_categories(data):
    churn_counts = data["churn_category"].value_counts()

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


def probability_to_text(probabilities):
    return [
        "висока" if p >= 0.75 else "середня" if 0.5 <= p < 0.75 else "низька"
        for p in probabilities
    ]


def make_predictions(data):
    try:
        # Перевірка наявності ідентифікаторного стовпця
        if "id" in data.columns:
            id_column = "id"
        elif "last_name" in data.columns:
            id_column = "last_name"
        else:
            return None, ["Не вдається визначити ідентифікаторний стовпець."]

        output = pd.DataFrame(data[id_column])
        # Завантаження моделі
        model = get_model(get_model_name())

        if get_model_name()=="decision_tree.pkl":
            # Виконання передбачень
            predictions = model.predict_proba(scale(data))[:, 1]
        else:
            predictions = model.predict_proba(scale(prepare_data(data)))[:, 1]

        # Додавання результатів передбачень до вихідних даних
        output["churn_category"] = probability_to_text(predictions)
        output["churn_probability"] = predictions

        print(">>", output)

        return output, None
    except Exception as e:
        return None, [str(e)]


def func(pct, allvals):
    absolute = int(pct / 100.0 * sum(allvals))
    return f"{absolute} з {sum(allvals)} ({pct:.1f}%)"


def predict_single_user(data):
    try:
        # Завантаження моделі
        model = get_model(get_model_name())
        # Прогнозування ймовірностей
        predictions = model.predict_proba(processing_input_data(data))[:, 1]
        data = pd.DataFrame()

        # Виведення ймовірностей
        print(f"Ймовірності прогнозування: {predictions}")

        # Встановлення ймовірності відтоку та категорії
        data["churn_category"] = probability_to_text(predictions)
        data["churn_probability"] = predictions

        return data
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return pd.DataFrame()

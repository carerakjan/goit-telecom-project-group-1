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


def visualize_churn_categories_bar(df):
    all_indicies = [
        "decision_tree.pkl",
        "logistic_regression_model.pkl",
        "svm_model_linear.pkl",
        "svm_model_poly.pkl",
        "svm_model_rbf.pkl",
        "neural_model_MLP.pkl",
        "svm_model_sigmoid.pkl",
    ]

    df = df.iloc[:, 1:4]
    df = df.groupby(["Модель", "Категорія відтоку"]).count().reset_index()
    df = df.pivot(columns=["Категорія відтоку"], index=["Модель"]).fillna(0)
    df_np = df.reset_index().to_numpy()

    for i in all_indicies:
        if i not in df.index:
            zero_count = len(df_np[0][1:])
            arr1 = np.array([i])
            arr2 = np.zeros(zero_count).astype(float)
            df_np = np.append(df_np, [np.concatenate((arr1, arr2))], axis=0)

    df_index = [arr[0] for arr in df_np]
    df_np = np.array([arr[1:] for arr in df_np]).astype(float)

    df = pd.DataFrame(
        df_np, columns=df["Вірогідність відтоку"].columns.to_list(), index=df_index
    )

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
    bottom_acc = None

    for i, col in enumerate(df.columns):
        ax.bar(df.index, df[col], label=col, bottom=bottom_acc)
        bottom_acc = df[col] if bottom_acc is None else bottom_acc + df[col]

    for idx in df.index:
        start = 0
        for col in df.columns:
            y = df.loc[idx, col]
            value = df.loc[idx, col]
            total = df.loc[idx, :].sum()
            if value:
                ax.text(
                    x=idx,
                    y=start + y / 2,
                    s=f"{round(100 * value / total, 1)}%",
                    fontsize=10,
                    ha="center",
                    color="w",
                )
            start += y

    plt.xticks(rotation=45, ha="right")
    ax.legend(title="Категорії відтоку")
    plt.ylabel("Кількість передбачень")
    plt.title("Розподіл категорій відтоку для кожної моделі")
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

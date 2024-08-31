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


def get_metrics_by_model(model_name: str):
    """
    Отримання метрик для конкретної моделі.

    :param model_name: Назва моделі.
    :return: Точність, пороги та поточний поріг.
    """
    model_name = model_name.split(".")[0]  # Видалення розширення файлу з назви моделі
    metrics = dict(load_metrics())  # Завантаження метрик
    precision, thresholds, current_threshold = metrics[
        model_name
    ]  # Отримання метрик для моделі
    return precision, thresholds, current_threshold


def plot_bagel_chart(model_name, current_threshold=1.0):
    """
    Побудова графіка у вигляді кільця (bagel chart) для точності моделі.

    :param model_name: Назва моделі.
    :param current_threshold: Поточний поріг для визначення точності.
    """
    precision, recall, thresholds = get_metrics_by_model(
        model_name=model_name
    )  # Отримання метрик
    fig, ax = plt.subplots(figsize=(6, 6))  # Створення фігури та осі для графіка
    prec = precision[1]  # Точність для даного порогу

    # Налаштування кольорів та радіусів
    wedge_colors = [
        "#00aaff" if prec > 0.9 else "#ff6347",  # Колір для заповненого сегмента
        "#e0e0e0",  # Колір для незаповненого сегмента
    ]
    radius = 0.4  # Радіус кільця

    # Знаходження відповідного значення точності для поточного порога
    idx = np.searchsorted(thresholds, current_threshold, side="right") - 1
    if idx < 0:
        idx = 0  # Захист від виходу за межі масиву
    precision_value = precision[idx]  # Точність для знайденого порогу

    # Сегменти для графіка
    filled_segment = precision_value * 100  # Заповнений сегмент
    remaining_segment = 100 - filled_segment  # Незаповнений сегмент

    # Побудова графіка у вигляді кільця
    wedges = [filled_segment, remaining_segment]

    plt.pie(
        wedges,
        colors=wedge_colors,
        startangle=90,
        counterclock=False,
        wedgeprops=dict(width=radius),  # Налаштування ширини кільця
    )

    # Налаштування тексту з поточним значенням точності
    plt.text(
        0,
        0,
        f"{precision_value:.2f}",  # Виведення точності у вигляді тексту
        ha="center",
        va="center",
        fontsize=20,
        color="#000000",
    )

    # Установлення однакових пропорцій для осей
    ax.set_aspect("equal")

    # Прибираємо осі
    plt.axis("off")

    # Відображення графіка у Streamlit
    st.pyplot(fig)


def plot_bagel_wrapper(model_name):
    """
    Обгортка для побудови графіка з метриками та графіка у вигляді кільця.

    :param model_name: Назва моделі.
    """
    # Створення двох колонок для розміщення елементів
    col1, col2 = st.columns(2)

    # Заповнення колонок
    with col1:
        st.header(f"Метрики моделі: {model_name}")  # Заголовок для колонок
        precision, thresholds, _ = get_metrics_by_model(model_name)  # Отримання метрик
        st.markdown(
            f"<p style='font-size: 1.5rem'>Модель показала точність:<br/>{precision[1]:.2f} при повноті: {thresholds[1]:.2f}</p>",
            unsafe_allow_html=True,  # Відображення тексту у HTML форматі
        )
        models_bar_plot(model_name)  # Побудова графіка з точностями інших моделей

    with col2:
        plot_bagel_chart(model_name)  # Побудова графіка у вигляді кільця


def models_bar_plot(model_name):
    """
    Побудова стовпчикового графіка для точностей моделей з виділенням конкретної моделі.

    :param model_name: Назва моделі для виділення.
    """
    data = load_metrics()  # Завантаження метрик

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
    plt.title("Дана модель серед інших")

    # Повертаємо розмітку
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # Відповідне розташування елементів
    plt.grid()  # Додаємо сітку для зручності

    # Відображення графіка у Streamlit
    st.pyplot(plt)


def plot_feature_importance(importances, feature_names, title):
    """
    Побудова графіка важливості ознак.

    :param importances: Масив важливостей ознак.
    :param feature_names: Список назв ознак.
    :param title: Заголовок графіка.
    """
    sorted_idx = np.argsort(importances)[
        ::-1
    ]  # Сортування важливостей у спадному порядку

    plt.figure(figsize=(10, 6))
    plt.barh(
        np.array(get_feature_titles(feature_names))[
            sorted_idx
        ],  # Назви ознак у порядку важливості
        importances[sorted_idx],  # Важливості ознак
        color="skyblue",
    )
    plt.xlabel("Важливість")
    plt.ylabel("Особливості")
    plt.title(title)
    plt.gca().invert_yaxis()  # Перевертання осі Y для відображення найбільш важливих ознак вгорі

    # Відображення графіка у Streamlit
    st.pyplot(plt)


def plot_logistic_regression_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для моделі логістичної регресії.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = get_model(model_name)  # Завантаження моделі

    if not hasattr(model, "coef_"):
        st.error("Завантажена модель не має атрибута 'coef_'.")
        return

    importances = np.abs(model.coef_[0])  # Важливість ознак у логістичній регресії
    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - Логістична регресія"
    )
    plot_bagel_wrapper(model_name)  # Побудова графіка у вигляді кільця


def plot_decision_tree_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для моделі дерева рішень.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = get_model(model_name)  # Завантаження моделі

    if not hasattr(model, "feature_importances_"):
        st.error("Завантажена модель не має атрибута 'feature_importances_'.")
        return

    importances = model.feature_importances_

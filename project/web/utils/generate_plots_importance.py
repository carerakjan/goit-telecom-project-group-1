import joblib  # Для завантаження моделі
import numpy as np  # Для обробки масивів даних
import matplotlib.pyplot as plt  # Для побудови графіків
import streamlit as st  # Для відображення графіків у Streamlit
import shap  # Для пояснення моделей за допомогою SHAP
import os
from sklearn.utils import shuffle
from web.utils.get_main_features import get_feature_titles


def plot_feature_importance(importances, feature_names, title):
    """
    Побудова графіка важливості ознак.

    :param importances: Масив важливостей ознак.
    :param feature_names: Список назв ознак.
    :param title: Заголовок графіка.
    """
    sorted_idx = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    plt.barh(
        np.array(get_feature_titles(feature_names))[sorted_idx],
        importances[sorted_idx],
        color="skyblue",
    )
    plt.xlabel("Важливість")
    plt.ylabel("Особливості")
    plt.title(title)
    plt.gca().invert_yaxis()

    st.pyplot(plt)


def plot_logistic_regression_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для моделі логістичної регресії.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "coef_"):
        st.error("Завантажена модель не має атрибута 'coef_'.")
        return

    importances = np.abs(model.coef_[0])
    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - Логістична регресія"
    )


def plot_decision_tree_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для моделі дерева рішень.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "feature_importances_"):
        st.error("Завантажена модель не має атрибута 'feature_importances_'.")
        return

    importances = model.feature_importances_
    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - Дерево рішень"
    )


def plot_svm_linear_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для лінійної SVM моделі.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "coef_"):
        st.error("Завантажена модель не має атрибута 'coef_'.")
        return

    importances = np.abs(model.coef_[0])
    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - Лінійний SVM"
    )


def plot_svm_poly_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для поліноміальної SVM моделі з використанням SHAP.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "decision_function"):
        st.error("Завантажена модель не має методу 'decision_function'.")
        return

    # Вибір 10 випадкових записів з X
    X_subset = shuffle(X, random_state=42)[:10]

    try:
        explainer = shap.KernelExplainer(
            model.decision_function, X_subset, nsamples=100
        )  # Використовуйте менше nsamples для прискорення
        shap_values = explainer.shap_values(X_subset)
        importances = np.abs(shap_values).mean(axis=0)
    except Exception as e:
        st.error(f"Помилка при використанні SHAP: {e}")
        return

    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - Поліноміальний SVM"
    )


def plot_svm_rbf_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для RBF SVM моделі з використанням SHAP.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "decision_function"):
        st.error("Завантажена модель не має методу 'decision_function'.")
        return

    # Вибір 10 випадкових записів з X для прискорення
    X_subset = shuffle(X, random_state=42)[:10]

    try:
        progress_bar = st.progress(0)
        # Використовуємо KernelExplainer для SVM моделей
        explainer = shap.KernelExplainer(model.decision_function, X_subset, nsamples=10)
        shap_values = explainer.shap_values(X_subset)
        progress_bar.progress(100)
        importances = np.abs(shap_values).mean(axis=0)
    except Exception as e:
        st.error(f"Помилка при використанні SHAP: {e}")
        return

    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - RBF SVM"
    )


def plot_mlp_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для MLP моделі.
    Зараз ця функція не реалізована.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "predict_proba"):
        st.error("Завантажена модель не має методу 'predict_proba'.")
        return

    # Визначення функції для прогнозування ймовірностей
    def predict_proba_fn(X):
        return model.predict_proba(X)

    try:
        st.warning("Функція для важливості ознак для MLP ще не реалізована.")
    except Exception as e:
        st.error(f"Помилка: {e}")
        return

    # Поки що немає реалізації для MLP


def plot_svm_sigmoid_importance(model_name, X, feature_names):
    """
    Побудова графіка важливості ознак для SVM моделі з сигмоїдною активацією з використанням SHAP.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model = joblib.load(os.path.join("project/models", model_name))

    if not hasattr(model, "predict"):
        st.error("Завантажена модель не має методу 'predict'.")
        return

    # Вибір 100 випадкових записів з X для прискорення
    X_subset = shuffle(X, random_state=42)[:100]

    try:
        progress_bar = st.progress(0)
        # Використовуємо Explainer для SVM моделей з predict
        explainer = shap.Explainer(model.predict, X_subset)
        shap_values = explainer(X_subset)
        progress_bar.progress(100)
        importances = np.abs(shap_values.values).mean(axis=0)
    except Exception as e:
        st.error(f"Помилка при використанні SHAP: {e}")
        return

    plot_feature_importance(
        importances, feature_names, "Важливість особливостей - SVM Sigmoid"
    )


def select_plot(model_name, X, feature_names):
    """
    Вибір та побудова графіка важливості ознак в залежності від типу моделі.

    :param model_name: Назва файлу моделі.
    :param X: Вхідні дані (фічі).
    :param feature_names: Список назв ознак.
    """
    model_functions = {
        "logistic_regression_model.pkl": plot_logistic_regression_importance,
        "decision_tree.pkl": plot_decision_tree_importance,
        "svm_model_linear.pkl": plot_svm_linear_importance,
        "svm_model_poly.pkl": plot_svm_poly_importance,
        "svm_model_rbf.pkl": plot_svm_rbf_importance,
        "neural_model_MLP.pkl": plot_mlp_importance,
        "svm_model_sigmoid.pkl": plot_svm_sigmoid_importance,
    }

    if model_name not in model_functions:
        st.error("Невірне ім'я моделі.")
        return

    model_function = model_functions[model_name]
    model_function(model_name, X, feature_names)

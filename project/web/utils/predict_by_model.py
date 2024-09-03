from web.utils.scale_data import scale, prepare_data
from web.utils.load_model import get_model, get_model_name
import streamlit as st

def get_predict(data):
    # Підготовка та масштабування даних
    processed_data = scale(prepare_data(data))

    # Отримання імені моделі
    model_name = get_model_name()

    # Список підтримуваних моделей
    supported_models = {
        "decision_tree.pkl",
        "logistic_regression_model.pkl",
        "svm_model_linear.pkl",
        "neural_model_MLP.pkl",
        "svm_model_sigmoid.pkl",
        "svm_model_poly.pkl",
        "svm_model_rbf.pkl"
    }

    # Перевірка, чи підтримується модель
    if model_name not in supported_models:
        st.write(f"Непідтримувана модель: {model_name}. Використовується модель за замовчуванням: decision_tree.pkl")
        
        model = get_model("decision_tree.pkl")
    else:
        model = get_model(model_name)
    # Повернення ймовірності позитивного класу
    return model.predict_proba(processed_data)[:, 1]
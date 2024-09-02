import streamlit as st
from web.utils.generate_plots_importance import select_plot
import pandas as pd


@st.dialog("Інформаційні данні щодо обранної моделі")  # instruction dialog window
def modal_dialog(select_model, X, feature_names):
    st.markdown('<style>[role="dialog"] {width:75vw}</style>', unsafe_allow_html=True)
    select_plot(select_model, X, feature_names)


@st.cache_data
def get_churn_csv():
    return pd.read_csv("project/data/internet_service_churn_scaled.csv").drop(
        columns=["churn"], errors="ignore"
    )


def render_model_bar(keys):
    # Створення двох колонок
    col1, col2 = st.columns(2)
    selectbox_key, button_key = keys

    # Заповнення колонок
    with col1:
        options = (
            "decision_tree.pkl",
            "logistic_regression_model.pkl",
            "svm_model_linear.pkl",
            "svm_model_poly.pkl",
            "svm_model_rbf.pkl",
            "neural_model_MLP.pkl",
            "svm_model_sigmoid.pkl",
        )

        default_value = st.session_state.selected_model

        # Отримання індексу значення по замовчуванню
        default_index = options.index(default_value)

        select_model = st.selectbox(
            "Оберіть модель для  використання ",
            options=options,
            key=selectbox_key,
            index=default_index,
        )

        # Обновление выбранной модели в session_state
        st.session_state.selected_model = select_model

    with col2:
        # Відступ зверху для відображення кнопки на рівні з селектором вибору моделі
        st.markdown('<p style="padding:0.36rem 0"></p>', unsafe_allow_html=True)

        if st.button("Переглянути важливість ознак", key=button_key):
            feature_names = [
                "is_tv_subscriber",
                "is_movie_package_subscriber",
                "subscription_age",
                "reamining_contract",
                "download_avg",
                "upload_avg",
                "download_over_limit",
            ]
            X = get_churn_csv()
            modal_dialog(st.session_state.selected_model, X, feature_names)

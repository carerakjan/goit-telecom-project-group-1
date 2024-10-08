import streamlit as st
import pandas as pd
from web.utils.business_logic_for_processing_data import (
    make_predictions,
    visualize_churn_categories,
)


def render_multi_tab():
    # st.header("Прогнозування для списку користувачів")

    uploaded_file = st.file_uploader(
        "Завантажте файл зі списком користувачів для прогнозування (формат CSV)",
        type=["csv"],
    )

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        if data is not None:
            st.success("Файл успішно завантажено!")

            st.subheader("Таблиця користувачів для прогнозування")
            st.write(data)
    else:
        data=None

    # Розміщення кнопок у верхній частині сторінки
    col1, col2 = st.columns([1, 1])  # Задайте співвідношення ширини колонок

    with col1:
        if st.button("Зробити прогнозування"):
            if data is not None:
                predicted_data, missing_columns = make_predictions(data)
                if predicted_data is not None:
                    st.subheader("Вірогідність відтоку:")

                    column_translation = {
                        'id': 'ID користувача',
                        'churn_category': 'Категорія відтоку',
                        'churn_probability': 'Ймовірність відтоку',
                    }

                    
                    translated_data = predicted_data.rename(columns=column_translation)
                    st.dataframe(translated_data, hide_index=True)

                    with col2:
                        st.subheader("Розподіл ймовірності відтоку:")
                        visualize_churn_categories(predicted_data)
                else:
                    if missing_columns:
                        missing_columns_str = ", ".join(missing_columns)
                        st.error(
                            f"Файл не містить всі необхідні колонки для прогнозування. Не вистачає колонок: {missing_columns_str}"
                        )
                    else:
                        st.error("Не вдалося провести прогнозування через помилку у даних.")
            else:
                st.error("Завантаже файл з данними зразок Тестовий файл в навігаційній панелі.")
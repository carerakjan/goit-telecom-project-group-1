import streamlit as st
import pandas as pd

from web.utils.business_logic_for_processing_data import (
    make_predictions,
    visualize_churn_categories_bar,
)


def render_single_tab():
    # st.header("Одиночне прогнозування")

    with st.form(key="single_prediction_form"):
        # Введення даних користувача
        is_tv_subscriber = st.selectbox(
            "Чи є підписником телевізійного пакету?", ["Так", "Ні"], key="tv_subscriber"
        )
        is_movie_package_subscriber = st.selectbox(
            "Чи є підписником пакету фільмів?", ["Так", "Ні"], key="movie_subscriber"
        )
        subscription_age = st.number_input(
            "Вік підписки (в місяцях)", min_value=0.0, max_value=12.0, value=0.0
        )
        reamining_contract = st.number_input(
            "Залишок контракту (в місяцях)", min_value=0.0, max_value=12.0, value=0.0
        )
        download_avg = st.number_input("Середній об'єм завантаження (Гб)", min_value=0.0, max_value=8830.0, value=0.0)
        upload_avg = st.number_input("Середній об'єм відвантаження (Гб)", min_value=0.0, max_value=906.0, value=0.0)
        download_over_limit = st.number_input("Перевищення ліміту завантаження (Гб)", min_value=0, max_value=14, value=0)
        

        # Кнопка для прогнозування
        submit_button = st.form_submit_button(label="Прогнозувати")

        if submit_button:
            data = {
                "is_tv_subscriber": 1 if is_tv_subscriber == "Так" else 0,
                "is_movie_package_subscriber": (
                    1 if is_movie_package_subscriber == "Так" else 0
                ),
                "subscription_age": subscription_age,
                "reamining_contract": reamining_contract,
                "download_avg": download_avg,
                "upload_avg": upload_avg,
                "download_over_limit": download_over_limit,
            }

            # Convert user input to DataFrame
            df = pd.DataFrame([data])
            predicted_data, missing_columns = make_predictions(df)

            if predicted_data is not None:
                st.session_state.user_count += 1      # increase user counter
                predicted_data["Модель"] = st.session_state.selected_model      # add chosen model to DataFrame
                predicted_data["Користувач"] = st.session_state.user_count

                st.session_state.all_data = pd.concat([st.session_state.all_data,  pd.concat([predicted_data, df], axis=1) ], ignore_index=True)       # concat DataFrames to final one
                st.success("Прогноз додано. Ви можете додати ще одного користувача.")
            else:
                if missing_columns:
                    missing_columns_str = ", ".join(missing_columns)
                    st.error(
                        f"Файл не містить всі необхідні колонки для прогнозування. Не вистачає колонок: {missing_columns_str}"
                    )
                else:
                    st.error("Не вдалося провести прогнозування через помилку у даних.")

    if not st.session_state.all_data.empty:
        st.subheader("Всі результати прогнозування:")

        st.dataframe(st.session_state.all_data, hide_index=True)
        st.subheader("Розподіл ймовірності відтоку:")
        visualize_churn_categories_bar(st.session_state.all_data)       # creating final Dataframe      






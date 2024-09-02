import streamlit as st
import pandas as pd

from web.utils.business_logic_for_processing_data import make_predictions


def render_single_tab():
    # st.header("Одиночне прогнозування")

    with st.form(key="single_prediction_form"):
        # Введення даних користувача
        is_tv_subscriber = st.selectbox(
            "Чи є підписником телевізійного пакету?", ["Так", "Ні"]
        )
        is_movie_package_subscriber = st.selectbox(
            "Чи є підписником пакету фільмів?", ["Так", "Ні"]
        )
        subscription_age = st.number_input(
            "Вік підписки (в місяцях)", min_value=0.0, value=0.0
        )
        reamining_contract = st.number_input(
            "Залишок контракту (в місяцях)", min_value=0.0, value=0.0
        )
        download_avg = st.number_input("Середній об'єм завантаження (Гб)", value=0.0)
        upload_avg = st.number_input("Середній об'єм відвантаження (Мб/с)", value=0.0)
        download_over_limit = st.number_input(
            "Перевищення ліміту завантаження (Гб)", value=0.0
        )

        # Кнопка для прогнозування
        submit_button = st.form_submit_button(label="Прогнозувати")

    # Обробка результату
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
            # Save result to session_state
            st.session_state.predictions.append(predicted_data)
            st.session_state.user_count += 1

            # Display results
            st.success("Прогноз додано. Ви можете додати ще одного користувача.")

        else:
            if missing_columns:
                missing_columns_str = ", ".join(missing_columns)
                st.error(
                    f"Файл не містить всі необхідні колонки для прогнозування. Не вистачає колонок: {missing_columns_str}"
                )
            else:
                st.error("Не вдалося провести прогнозування через помилку у даних.")

    # Відображення результатів всіх попередніх користувачів
    if st.session_state.predictions:
        st.subheader("Всі результати прогнозування:")
        for i, prediction in enumerate(st.session_state.predictions, start=1):
            st.write(f"Вірогідність відтоку для користувача {i}:")
            st.dataframe(prediction, hide_index=True)

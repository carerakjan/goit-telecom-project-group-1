import streamlit as st
from web.utils.business_logic_for_processing_data import predict_single_user

def render_single_tab():
    st.header('Одиночне прогнозування')

    # Форма для введення даних користувача
    with st.form(key='single_prediction_form'):
        # Поля введення
        is_tv_subscriber = st.selectbox('Чи є підписником телевізійного пакету?', ['Так', 'Ні'])
        is_movie_package_subscriber = st.selectbox('Чи є підписником пакету фільмів?', ['Так', 'Ні'])
        subscription_age = st.number_input('Вік підписки (в місяцях)', min_value=0, value=0)
        remaining_contract = st.number_input('Залишок контракту (в місяцях)', min_value=0, value=0)
        download_avg = st.number_input('Середній обсяг завантажень (ГБ)', value=0.0)
        upload_avg = st.number_input('Середній обсяг відвантажень (ГБ)', value=0.0)
        download_over_limit = st.number_input('Перевищення ліміту завантаження (Гб)', value=0.0)

        # Додаємо кнопку для подання форми
        submit_button = st.form_submit_button(label='Прогнозувати')

        # Кнопка подання форми
        if submit_button:
            # Конвертуємо вибрані значення у відповідні типи
            data = {
                'is_tv_subscriber': 1 if is_tv_subscriber == 'Так' else 0,
                'is_movie_package_subscriber': 1 if is_movie_package_subscriber == 'Так' else 0,
                'subscription_age': subscription_age,
                'remaining_contract': remaining_contract,
                'download_avg': download_avg,
                'upload_avg': upload_avg,
                'download_over_limit': download_over_limit
            }

            # Виклик функції прогнозування
            predict_single_user(data)

            # Виводимо зібрані дані (або використовуємо їх для прогнозу)
            #st.write('Введені дані:')
            #st.write(f'Чи є підписником телевізійного пакету: {data["is_tv_subscriber"]}')
            #st.write(f'Чи є підписником пакету фільмів: {data["is_movie_package_subscriber"]}')
            #st.write(f'Вік підписки: {data["subscription_age"]}')
            #st.write(f'Залишок контракту: {data["remaining_contract"]}')
            #st.write(f'Середній обсяг завантажень: {data["download_avg"]}')
            #st.write(f'Середній обсяг відвантажень: {data["upload_avg"]}')
            #st.write(f'Перевищення ліміту завантаження: {data["download_over_limit"]}')

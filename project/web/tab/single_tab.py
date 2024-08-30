import streamlit as st
from web.utils.business_logic_for_processing_data import predict_single_user

def render_single_tab():
    st.header('Одиночне прогнозування')

    # Перевіряємо, чи є змінна в стані сесії, якщо ні - ініціалізуємо її
    if 'user_count' not in st.session_state:
        st.session_state.user_count = 1

    with st.form(key=f'single_prediction_form_{st.session_state.user_count}'):
        # Поля введення даних
        is_tv_subscriber = st.selectbox('Чи є підписником телевізійного пакету?', ['Так', 'Ні'])
        is_movie_package_subscriber = st.selectbox('Чи є підписником пакету фільмів?', ['Так', 'Ні'])
        subscription_age = st.number_input('Вік підписки (в місяцях)', min_value=0, value=0)
        reamining_contract = st.number_input('Залишок контракту (в місяцях)', min_value=0, value=0)
        download_avg = st.number_input('Середня швидкість завантаження (Мб/с)', value=0.0)
        upload_avg = st.number_input('Середня швидкість відвантаження (Мб/с)', value=0.0)
        download_over_limit = st.number_input('Перевищення ліміту завантаження (Гб)', value=0.0)

        # Кнопка відправки даних
        submit_button = st.form_submit_button(label='Прогнозувати')

    # Обробка форми
    if submit_button:
        data = {
            'is_tv_subscriber': 1 if is_tv_subscriber == 'Так' else 0,
            'is_movie_package_subscriber': 1 if is_movie_package_subscriber == 'Так' else 0,
            'subscription_age': subscription_age,
            'reamining_contract': reamining_contract,
            'download_avg': download_avg,
            'upload_avg': upload_avg,
            'download_over_limit': download_over_limit
        }

        predicted_data = predict_single_user(data)

        st.subheader('Результати прогнозування:')
        st.dataframe(predicted_data, hide_index=True)

        # Запитуємо у користувача, чи хоче він додати іншого користувача
        another_user = st.button('Додати іншого користувача')

        if another_user:
            # Збільшуємо лічильник для унікального ключа форми
            st.session_state.user_count += 1
            st.experimental_rerun()

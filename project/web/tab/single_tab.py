import streamlit as st
from web.utils.business_logic_for_processing_data import predict_single_user

def render_single_tab():
    st.header('Одиночне прогнозування')

    # Ініціалізація збережених результатів у session_state
    if 'user_count' not in st.session_state:
        st.session_state.user_count = 1
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []

    with st.form(key=f'single_prediction_form_{st.session_state.user_count}'):
        # Введення даних користувача
        is_tv_subscriber = st.selectbox('Чи є підписником телевізійного пакету?', ['Так', 'Ні'])
        is_movie_package_subscriber = st.selectbox('Чи є підписником пакету фільмів?', ['Так', 'Ні'])
        subscription_age = st.number_input('Вік підписки (в місяцях)', min_value=0, value=0)
        reamining_contract = st.number_input('Залишок контракту (в місяцях)', min_value=0, value=0)
        download_avg = st.number_input('Середня швидкість завантаження (Мб/с)', value=0.0)
        upload_avg = st.number_input('Середня швидкість відвантаження (Мб/с)', value=0.0)
        download_over_limit = st.number_input('Перевищення ліміту завантаження (Гб)', value=0.0)

        # Кнопка для прогнозування
        submit_button = st.form_submit_button(label='Прогнозувати')

    # Обробка результату
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

        # Збереження результату у session_state
        st.session_state.predictions.append(predicted_data)

        # Збільшення лічильника користувачів
        st.session_state.user_count += 1

        # Відображення результатів
        st.success("Прогноз додано. Ви можете додати ще одного користувача.")

    # Відображення результатів всіх попередніх користувачів
    if st.session_state.predictions:
        st.subheader('Всі результати прогнозування:')
        for i, prediction in enumerate(st.session_state.predictions, start=1):
            st.write(f"Результати для користувача {i}:")
            st.dataframe(prediction, hide_index=True)

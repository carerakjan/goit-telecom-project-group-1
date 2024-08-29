import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#from plots import setData

# Функція для перевірки наявності необхідних колонок
def check_columns(data, required_columns):
    missing_columns = [col for col in required_columns if col not in data.columns]
    return missing_columns

# Функція для завантаження даних
def load_data(file):
    try:
        df = pd.read_csv(file)  # Завантаження даних з файлу CSV
        return df
    except Exception as e:
        st.error(f'Помилка завантаження даних: {str(e)}')
        return None

def render_multi_tab():
    print('111')
    st.header('Передбачення для списку юзерів')

    uploaded_file = st.file_uploader("Завантажте файл зі списком користувачів для прогнозування формат csv", type=['csv'])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        if data is not None:
            st.success('Файл успішно завантажено!')

            # Відображення таблиці користувачів
            st.subheader('Таблиця користувачів для передбачення')

            # Розділення екрана на колонки
            col1, col2 = st.columns([3, 1])  # Відсоткові відношення ширини колонок

            # У першій колонці відображаємо таблицю користувачів
            # Вибір колонки на основі наявності 'id' або 'last_name'
            required_column = 'id' if 'id' in data.columns else 'last_name' if 'last_name' in data.columns else 'id'

            if required_column is not None:
                required_columns = [
                    required_column,
                    'is_tv_subscriber',
                    'is_movie_package_subscriber',
                    'subscription_age',
                    'reamining_contract',
                    'download_avg',
                    'upload_avg',
                    'download_over_limit'
                ]


                col1.write(data)

                
                missing_columns = [col for col in required_columns if col not in data.columns]

                if col2.button('Перевірити формат'):
                    if not missing_columns:
                        st.write("Формат файлу відповідає заданим вимогам. Усі необхідні колонки присутні.")
                    else:
                        missing_columns_str = ', '.join(missing_columns)
                        error_message = f"Формат файлу не відповідає вимогам. Не вистачає колонок: {missing_columns_str}"
                        st.markdown(f'<p style="color:red">{error_message}</p>', unsafe_allow_html=True)

                if col2.button('Зробити передбачення'):
                    print('1111')
                   # setData(data)
                    
            else:
                st.warning("Не вдалося знайти жодну з необхідних колонок ('id' або 'last_name') в DataFrame.")
       


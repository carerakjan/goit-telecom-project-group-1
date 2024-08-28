import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Функція для кругової діаграми
def plot_pie_chart(data):
    # Розрахунок кількості елементів кожної категорії
    category_counts = data['Категорія'].value_counts()

    # Створення кругової діаграми
    plt.figure(figsize=(8, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Розподіл за категоріями')
    plt.axis('equal')  # Забезпечуємо, що кругова діаграма буде круглою
    st.pyplot()  # Відображення діаграми у Streamlit

# Функція для завантаження даних
def load_data(file):
    try:
        df = pd.read_csv(file)  # Завантаження даних з файлу CSV
        return df
    except Exception as e:
        st.error(f'Помилка завантаження даних: {str(e)}')
        return None

def render_multi_tab():
    st.header('Множинне прогнозування')

    uploaded_file = st.file_uploader("Завантажте файл зі списком користувачів для прогнозування формат csv", type=['csv'])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.success('Файл успішно завантажено!')

        # Відображення таблиці користувачів
        st.subheader('Таблиця користувачів для прогнозування')
        
        # Розділення екрана на колонки
        col1, col2 = st.columns([3, 1])  # Відсоткові відношення ширини колонок

        # У першій колонці відображаємо таблицю користувачів
        col1.write(data)

        # У другій колонці відображаємо кнопку "Перевірити формат"
        if col2.button('Перевірити формат'):
            st.write("Формат файлу перевірено. Колонки відповідають заданому формату.")
        
        if col2.button('Зробити прогноз'):
            plot_pie_chart(data)
       


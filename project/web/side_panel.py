import streamlit as st
import pandas as pd
from web.instruction_dialog import show_instruction_dialog


@st.dialog("Зразок файлу", width="large")
def example():
    showcsv = pd.read_csv("project/data/users.csv")
    st.header("Перевірте відповідність колонок та даних для свого файлу")
    st.write(showcsv)

@st.dialog("Обмеження введення показників для прогнозування",width="large")
def max_value_list():
    st.header("Лист мінімальних та максимальних значеннь для прогнозування")

    data = {
        "Поле": [
            "Вік підписки (в місяцях)",
            "Залишок контракту (в місяцях)",
            "Середній об'єм завантаження (Гб)",
            "Середній об'єм відвантаження (Гб)",
            "Перевищення ліміту завантаження (Гб)"
        ],
        "Мінімальні значення": [
            "0 місяців",
            "0 місяців",
            "0 Гб",
            "0 Гб",
            "0 Гб"
        ],"Максимальні значення": [
            "12 місяців",
            "12 місяців",
            "8830 Гб",
            "906 Гб",
            "14 Гб"
        ]

    }

    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True)



def toggle_layout_home():
    st.session_state.hide_layout = not st.session_state.hide_layout


def refresh_page():
    # Скидання показу результатів і очищення збережених прогнозів
    st.session_state.all_data = pd.DataFrame(
        columns=["Користувач", "Категорія відтоку", "Вірогідність відтоку", "Модель"]
    )  # Очищення списку прогнозів
    st.session_state.user_count = 0  # Скидання лічильника користувачів


def base():

    st.sidebar.image(
        "project/web/resources/images/logo.png", use_column_width=False, width=100
    )

    st.sidebar.markdown(
        "Цей додаток дозволяє аналізувати клієнтські дані та визначати ймовірність припинення використання послуги."
    )

    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Повернутися на головну 🏠", on_click=toggle_layout_home):
        pass
    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Інструкція користування 📄"):
        show_instruction_dialog()
    # Кнопка "Зразок файлу"
    if st.sidebar.button("Тестовий файл 📄"):
        example()
    
    if st.sidebar.button("Вимоги показників введення 📋"):
        max_value_list()


    # Кнопка "Оновити"
    if st.sidebar.button("Оновити 🔄", on_click=refresh_page):
        pass

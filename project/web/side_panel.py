import streamlit as st
import pandas as pd

@st.dialog("Instruction", width="large")         
def inst():
    with open('project/web/resources/docs/instructions_for_the_User.txt', 'r', encoding='utf-8') as file:
      instructions = file.read()
      st.write(instructions)


@st.dialog("Зразок файлу", width="large")         
def example():
    showcsv = pd.read_csv("project/data/users.csv")
    st.header("Перевірте відповідність колонок та даних для свого файлу")
    st.write(showcsv)

def toggle_layout_home():
    st.session_state.hide_layout = not st.session_state.hide_layout

def refresh_page():
    # Скидання показу результатів і очищення збережених прогнозів
    st.session_state.show_results = False  # Забезпечує, що результати не відображатимуться
    st.session_state.predictions = []  # Очищення списку прогнозів
    st.session_state.user_count = 1  # Скидання лічильника користувачів

def base():

    st.sidebar.image("project/web/resources/images/logo.png", use_column_width=False, width=100)

    st.sidebar.markdown("Цей додаток дозволяє аналізувати клієнтські дані та визначати ймовірність припинення використання послуги.")

    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Повернутися на головну 🏠", on_click=toggle_layout_home):
        pass
    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Інструкція користування 📄"):
        inst()
    # Кнопка "Зразок файлу"
    if st.sidebar.button("Тестовий файл 📄"):
        example()
    

    # Кнопка "Оновити"
    if st.sidebar.button("Оновити 🔄", on_click=refresh_page):
        pass



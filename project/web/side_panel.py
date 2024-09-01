import streamlit as st
import pandas as pd

@st.dialog("Instruction", width="large")         
def inst():
    with open('project/web/resources/docs/Instructions_for_the_User.txt', 'r', encoding='utf-8') as file:
      instructions = file.read()
      st.write(instructions)


@st.dialog("Зразок файлу", width="large")         
def example():
    showcsv = pd.read_csv("project/data/users.csv")
    st.header("Перевірте відповідність колонок та даних для свого файлу")
    st.write(showcsv)

def base():
    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Повернутися на головну 🏠"):
        pass
    # Кнопка "Повернутися на головну"
    if st.sidebar.button("Інструкція користування 📄"):
        inst()
    # Кнопка "Зразок файлу"
    if st.sidebar.button("Тестовий файл 📄"):
        example()
    

    # Кнопка "Оновити"
    if st.sidebar.button("Оновити 🔄"):
       
        pass



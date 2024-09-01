import streamlit as st
from web.tab.single_tab import render_single_tab
from web.tab.multi_tab import render_multi_tab
from web.models_bar import render_model_bar


def render_tabs():
    # Створення вкладок
    tab1, tab2 = st.tabs(["Одиночне прогнозування", "Передбачення для списку юзерів"])

    # Вміст вкладок
    with tab1:
        st.header("Одиночне прогнозування")
        render_model_bar(["selectbox1", "button1"])
        render_single_tab()

    with tab2:
        st.header("Передбачення для списку юзерів")
        render_model_bar(["selectbox2", "button2"])
        render_multi_tab()

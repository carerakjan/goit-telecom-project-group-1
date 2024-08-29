import streamlit as st

from app.tab.multi_tab import render_multi_tab
from app.tab.single_tab import render_single_tab


def base():
    st.title('Передбачення для клієнтів')

    # Вкладки
    tabs = st.sidebar.radio("Виберіть тип передбачення ", ("Одиночне прогнозування", "Прогнозування множинне"))

    if tabs == "Одиночне передбачення":
        render_single_tab()

    elif tabs == "Множинне предбачення":
        render_multi_tab()
        


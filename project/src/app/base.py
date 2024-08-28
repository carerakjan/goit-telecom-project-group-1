import streamlit as st

from app.tab.multi_tab import render_multi_tab
from app.tab.single_tab import render_single_tab


def base():
    st.title('Прогнозування клієнтів')

    # Вкладки
    tabs = st.sidebar.radio("Виберіть тип прогнозування", ("Одиночне прогнозування", "Прогнозування множинне"))

    if tabs == "Одиночне прогнозування":
        render_single_tab()

    elif tabs == "Прогнозування множинне":
        render_multi_tab()
        


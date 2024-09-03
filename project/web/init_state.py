import streamlit as st
import pandas as pd


def init_state():
    st.session_state.setdefault("hide_layout", False)
    st.session_state.setdefault("selected_model", "decision_tree.pkl")
    st.session_state.setdefault("predictions", [])
    st.session_state.setdefault("user_count", 0)
    st.session_state.setdefault("all_data", pd.DataFrame(columns=["Користувач", "Категорія відтоку", "Вірогідність відтоку", "Модель"]))
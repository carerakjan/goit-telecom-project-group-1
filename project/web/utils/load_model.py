import streamlit as st
import os
import joblib

# Инициализация session_state
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "decision_tree.pkl"

@st.cache_data
def get_model(model_name):
    return joblib.load(os.path.join("project/models", model_name))


def get_model_name():
    model_name = st.session_state.selected_model
    if model_name is None:
        st.error("Модель не обрана.")
        return
    return model_name
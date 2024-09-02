import streamlit as st
import os
import joblib

@st.cache_resource
def get_model(model_name):
    return joblib.load(os.path.join("project/models/new_models", model_name))


def get_model_name():
    model_name = st.session_state.selected_model
    if model_name is None:
        st.error("Модель не обрана.")
        return
    return model_name

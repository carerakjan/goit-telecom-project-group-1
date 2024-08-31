import streamlit as st
import os
import joblib


@st.cache_data
def get_model(model_name):
    return joblib.load(os.path.join("project/models", model_name))

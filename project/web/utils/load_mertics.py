import pickle
import streamlit as st

# @st.cache_data
def load_metrics(file_path="project/data/metrics.pkl"):
    # Завантаження даних з Pickle файлу
    with open(file_path, "rb") as f:
        metrics = pickle.load(f)
    return metrics

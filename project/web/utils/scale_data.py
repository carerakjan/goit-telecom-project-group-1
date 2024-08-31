import pickle
import streamlit as st
from web.utils.get_main_features import main_features


@st.cache_data
def get_scaler():
    with open("project/data/scaler.pkl", "rb") as file:
        return pickle.load(file)


def scale(df):
    return get_scaler().transform(main_features(df))

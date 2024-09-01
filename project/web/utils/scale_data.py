import pickle
import streamlit as st
import pandas as pd  # Для роботи з даними у форматі DataFrame
from web.utils.get_main_features import main_features


@st.cache_resource
def get_scaler():
    with open("project/data/scaler.pkl", "rb") as file:
        return pickle.load(file)


def scale(df):
    return get_scaler().transform(main_features(df))


def prepare_data(df):
    df.drop(columns=["bill_avg", "service_failure_count", "id"], errors="ignore")
    # Замінюємо пусті значення на NaN
    df.replace("", pd.NA, inplace=True)

    # Перетворюємо всі стовпці на числові значення
    df = df.apply(pd.to_numeric, errors="coerce")
    # Замінюємо NaN на нулі
    df.fillna(0, inplace=True)
    df = df.apply(pd.to_numeric, errors="coerce").astype("float64")
    df = df.round(2)

    return df

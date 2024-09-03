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
    columns_to_drop = ["bill_avg", "service_failure_count", "id"]

    # Check if columns exist before dropping
    existing_columns = df.columns.tolist()
    columns_to_drop = [col for col in columns_to_drop if col in existing_columns]

    if columns_to_drop:
        df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

    # Замінюємо пусті значення на NaN
    df.replace("", pd.NA, inplace=True)

    # Перетворюємо всі стовпці на числові значення
    df = df.apply(pd.to_numeric, errors="coerce")

    # Замінюємо NaN на нулі
    df.fillna(0, inplace=True)

    # Опціонально, якщо потрібно округлити значення до двох знаків після коми
    df = df.round(2)

    # Перетворюємо всі стовпці на float64
    df = df.astype("float64")

    return df

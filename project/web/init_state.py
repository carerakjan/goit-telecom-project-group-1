import streamlit as st


def init_state():
    if "hide_layout" not in st.session_state:
        st.session_state.hide_layout = False

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "decision_tree.pkl"

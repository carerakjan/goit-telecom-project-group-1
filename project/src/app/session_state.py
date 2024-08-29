import streamlit as st

from app.landing_page import landing_page
from app.base import base

def session():
    if 'hide_layout' not in st.session_state:
        st.session_state.hide_layout = False

    if not st.session_state.hide_layout:
        landing_page()
    else:
        base()


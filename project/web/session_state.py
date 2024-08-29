import streamlit as st

from web.landing_page import landing_page
from web.side_panel import base

def session():
    if 'hide_layout' not in st.session_state:
        st.session_state.hide_layout = False

    if not st.session_state.hide_layout:
        landing_page()
    else:
        base()

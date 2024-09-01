import streamlit as st
from web.tabs import render_tabs

from web.landing_page import landing_page
from web.side_panel import base
from web.init_state import init_state


def start():
    init_state()

    if not st.session_state.hide_layout:
        landing_page()
    else:
        render_tabs()
        base()

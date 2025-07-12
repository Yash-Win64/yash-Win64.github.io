import os
import streamlit as st

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "../assets/style.css")
    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ style.css file not found in /assets.")


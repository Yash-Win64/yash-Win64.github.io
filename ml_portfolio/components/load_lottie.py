import os
import json
import streamlit as st

def load_lottie(filename):
    path = os.path.join(os.path.dirname(__file__), "../assets", filename)
    if not os.path.isfile(path):
        st.error(f"❌ Animation file not found: {path}")
        return None
    with open(path, "r") as f:
        return json.load(f)

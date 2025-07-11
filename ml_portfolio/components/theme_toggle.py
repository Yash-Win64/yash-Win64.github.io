# components/theme_toggle.py
import streamlit as st

def theme_toggle(key="theme_toggle"):
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"

    # Toggle for dark/light mode
    dark_mode = st.toggle("🌗 Dark Mode", value=(st.session_state["theme"] == "dark"), key=key)
    st.session_state["theme"] = "dark" if dark_mode else "light"

    # Apply theme to root element
    st.markdown(f"""
    <script>
        const app = window.parent.document.querySelector('.stApp');
        if (app) {{
            app.setAttribute('data-theme', '{st.session_state["theme"]}');
        }}
    </script>
    """, unsafe_allow_html=True)



import streamlit as st
import json
from streamlit_lottie import st_lottie

# Set page config
st.set_page_config(page_title="Yash's ML Portfolio", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Lottie animation
def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

hello_anim = load_lottie("assets/hello.json")

# Hero Section
st_lottie(hello_anim, height=250)
st.title("Hi, I'm Yash Mishra 👋")
st.subheader("Machine Learning & Data Analytics Enthusiast")
st.markdown("""
🎓 B.Tech CSE (AI & ML) @ SRMGPC  
🧠 Skills: Python, Pandas, SQL, scikit-learn ,PowerBi, Excel ,Numpy, Data Analysis , Git , VsCode , Jupyter Notebook
💼 Role Interests: Data Analyst | ML Engineer  
📫 Let’s explore my work!
""")

# Next button to go to Projects
if st.button("🚀 Next: View My Projects"):
    st.switch_page("pages/Home.py")


  # Navigates to your existing projects page


import streamlit as st
import json
from streamlit_lottie import st_lottie
import os
from components.load_css import load_css
# Page config
st.set_page_config(page_title="About – Yash Mishra", layout="wide")

# Load CSS

load_css()


# Load Lottie animation
def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

hello_anim = load_lottie("assets/hello.json")

# Hero Section
st_lottie(hello_anim, height=250)
st.title("👋 About Me – Yash Mishra")
st.subheader("Machine Learning & Data Analytics Enthusiast")

# Professional Overview
st.markdown("""
I'm a final-year **B.Tech CSE (AI & ML)** student at **SRMGPC**, passionate about solving real-world problems with data-driven solutions.

### 🛠️ Skills & Tools
- **Languages**: Python, SQL
- **Libraries**: Pandas, NumPy, scikit-learn, Matplotlib, Seaborn
- **Tools**: Power BI, Excel, Git, Jupyter Notebook, VS Code, Streamlit

### 📌 Interests
- Data Analysis & Business Insights
- Machine Learning & Model Optimization
- Real-time Analytics & Interactive Dashboards

### 🎯 Goals
I aspire to work as a **Data Analyst or ML Engineer**, building scalable tools that make a real impact. I enjoy creating end-to-end projects and constantly learning new technologies.

### 📫 Let's Explore My Work
""")

# Next button
if st.button("🚀 Next: View My Projects"):
    st.switch_page("pages/Home.py")


with open("assets/resume_yash.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📥 Download My Resume (PDF)",
    data=PDFbyte,
    file_name="Yash_Mishra_Resume.pdf",
    mime="application/pdf",
    use_container_width=True
)

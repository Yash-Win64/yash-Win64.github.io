import streamlit as st
import json
from streamlit_lottie import st_lottie
import os
from components.load_css import load_css
from components.load_lottie import load_lottie

st.set_page_config(page_title="About – Yash Mishra", layout="wide")
load_css()


hello_anim = load_lottie("hello.json")
if hello_anim:
    st_lottie(hello_anim, height=250)

st.title("👋 About Me – Yash Mishra")
st.subheader("Machine Learning & Data Analytics Enthusiast")
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

if st.button("🚀 Next: View My Projects"):
    st.switch_page("pages/Home.py")

pdf_path = os.path.join("assets", "resume_yash.pdf")
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="📥 Download My Resume (PDF)",
            data=pdf_file.read(),
            file_name="Yash_Mishra_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
else:
    st.error("❌ Resume file not found.")

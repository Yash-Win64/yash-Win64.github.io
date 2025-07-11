import streamlit as st
from components.project_card import project_card
import json
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(page_title="Projects – Yash", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load animation
def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

ml_anim = load_lottie("assets/ml.json")
st_lottie(ml_anim, height=150)

st.title("🚀 Featured Projects")

project_card(
    title="Ad Click Prediction",
    description="Predict whether a user clicks on an ad based on session info.",
    image="assets/images/ad_click.png",
    link="pages/projects/1_Ad_Click_Prediction.py",
    github="https://github.com/yourusername/ad-click-predictor",
    tags=["Logistic Regression", "Random Forest", "EDA"]
)

project_card(
    title="Credit Card Fraud Detection",
    description="Detect fraud in card transactions using ensemble models and SMOTE.",
    image="assets/images/fraud.png",
    link="pages/projects/2_Credit_Card_Fraud_Detection.py",
    github="https://github.com/yourusername/credit-card-fraud",
    tags=["SMOTE", "Imbalanced Data", "Classification"]
)

project_card(
    title="Movie Recommendation System",
    description="Suggest movies using collaborative filtering and cosine similarity.",
    image="assets/images/movie.png",
    link="pages/projects/3_Movie_Recommendation_System.py",
    github="https://github.com/yourusername/movie-recommender",
    tags=["Recommendation", "Collaborative Filtering", "Cosine Similarity"]
)

project_card(
    title="SMS Spam Detection",
    description="Classify messages as spam or ham using Naive Bayes and text preprocessing.",
    image="assets/images/spam.png",
    link="pages/projects/4_Spam_SMS_Detection.py",
    github="https://github.com/yourusername/sms-spam-detector",
    tags=["NLP", "Naive Bayes", "Text Classification"]
)

st.markdown("---")
st.markdown("📚 Want to read more?")

if st.button("🧠 Read My Blogs"):
    st.switch_page("pages/7_Blogs.py")
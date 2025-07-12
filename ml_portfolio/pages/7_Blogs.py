# pages/7_Blogs.py
import streamlit as st
import os
from components.load_css import load_css

# Page config
st.set_page_config(page_title="🧠 Blogs – Yash Mishra", layout="wide")

# Load CSS
load_css()

st.title("🧠 My Project Blogs")
st.markdown("Here I break down the concepts and learnings behind each of my machine learning projects.")

# -----------------------------------------
# 📈 Blog 1: Ad Click Prediction
# -----------------------------------------
st.header("📈 How I Built the Ad Click Prediction Model")

st.markdown("""
This project aims to predict whether a user will click on an advertisement using demographic and behavioral data.

### 🔍 Dataset Insights:
- Features include Age, Area Income, Daily Time Spent, Internet Usage, and Timestamp.
- Target column: `Clicked on Ad`.

### 🛠️ Steps Followed:
1. **EDA**: Explored distributions and correlations.
2. **Feature Engineering**:
   - Extracted Hour and Day from Timestamp.
   - Removed redundant columns.
3. **Modeling**:
   - Trained Logistic Regression and Random Forest.

### ✅ Outcome:
- Random Forest achieved 96–97% accuracy.
- Most influential features: Daily Time Spent on Site and Age.
""")

st.markdown("---")

# -----------------------------------------
# 🔒 Blog 2: Credit Card Fraud Detection
# -----------------------------------------
st.header("🔒 Solving Class Imbalance in Credit Card Fraud Detection")

st.markdown("""
Fraud detection is challenging due to highly **imbalanced data** — fraud accounts for < 0.2% of all records.

### 🧾 Dataset:
- 284K transactions, anonymized features (V1 to V28).
- Target: `Class` (1 = Fraud, 0 = Genuine).

### 🛠️ Approach:
1. Used **SMOTE** to oversample fraud cases.
2. Trained multiple classifiers:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - AdaBoost

### 📊 Key Metrics:
- Focused on **Precision**, **Recall**, and **F1-Score**.
- AdaBoost and Random Forest yielded the best trade-off between detecting fraud and avoiding false alarms.
""")

st.markdown("---")


# -----------------------------------------
# 🎬 Blog 3: Movie Recommendation System
# -----------------------------------------
st.header("🎬 Cosine Similarity in Movie Recommendation System")

st.markdown("""
I built a system that recommends similar movies using **content-based filtering** and **cosine similarity**.

### 🎥 Dataset:
- `movies.csv` with titles, genres, and metadata.
- `ratings.csv` for user preferences.

### 🔍 Approach:
1. **Preprocessing**:
   - Combined relevant metadata (genres, keywords).
   - Used TF-IDF Vectorization to convert text into vectors.

2. **Similarity Calculation**:
   - Used **Cosine Similarity** to find closeness between movies.

3. **User Input Based Suggestions**:
   - Enter a movie name → returns top 5 similar movies.

### ✅ Outcome:
- Simple, effective recommendation engine.
- Great starting point before switching to collaborative filtering or deep learning.
""")

st.markdown("---")


# -----------------------------------------
# 💬 Blog 4: SMS Spam Detection
# -----------------------------------------
st.header("💬 SMS Spam Classification Using NLP")

st.markdown("""
The goal was to classify SMS messages as **Spam** or **Ham** (Not Spam) using Natural Language Processing techniques.

### 📄 Dataset Overview:
- ~5,500 labeled SMS messages.
- Two columns: `v1` (label) and `v2` (text message).

### 🛠️ Process:
1. **Preprocessing**:
   - Lowercasing, removing punctuation/numbers.
   - Tokenization, Stopword Removal, and Stemming.
2. **Vectorization**:
   - Used `CountVectorizer` for Bag-of-Words representation.
3. **Model**:
   - Trained a **Multinomial Naive Bayes** classifier.

### ✅ Results:
- Achieved ~98% accuracy.
- Lightweight and interpretable model with fast inference.
""")

st.markdown("---")


# Navigation
if st.button("📫 Contact Me"):
    st.switch_page("pages/6_Contact.py")



if st.button("⬅ Back to Ad Click Project"):
    st.switch_page("pages/Home.py")

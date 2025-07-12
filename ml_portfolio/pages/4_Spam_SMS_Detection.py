import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Ensure NLTK downloads
nltk.download('stopwords')

st.title("📨 SMS Spam Detection")
st.markdown("This app uses a Naive Bayes classifier to detect whether a message is **Spam** or **Ham** (not spam).")

# Load dataset
try:
    df = pd.read_csv("data/spam.csv", encoding="ISO-8859-1")[['v1', 'v2']]
    df.columns = ['label', 'message']
    st.success("✅ Loaded dataset from `data/spam.csv`")
except Exception as e:
    st.error("❌ Failed to load the dataset. Make sure `data/spam.csv` exists and has correct format.")
    st.stop()

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Encode labels
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# Preprocess
ps = PorterStemmer()
corpus = []

for msg in df['message']:
    msg = re.sub('[^a-zA-Z]', ' ', msg)
    msg = msg.lower()
    words = msg.split()
    words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    corpus.append(' '.join(words))

# Vectorize
vectorizer_type = st.radio("🔢 Choose vectorizer", ['CountVectorizer', 'TfidfVectorizer'])
if vectorizer_type == 'CountVectorizer':
    vectorizer = CountVectorizer(max_features=2500)
else:
    vectorizer = TfidfVectorizer(max_features=2500)

X = vectorizer.fit_transform(corpus).toarray()
y = df['label_num']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model selection
model_option = st.selectbox("🤖 Choose Classifier", ['MultinomialNB', 'BernoulliNB', 'Logistic Regression'])
if model_option == 'MultinomialNB':
    model = MultinomialNB(alpha=0.1)
elif model_option == 'BernoulliNB':
    model = BernoulliNB()
else:
    model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Results
acc = accuracy_score(y_test, y_pred)
st.subheader("✅ Accuracy")
st.write(f"**{acc*100:.2f}%**")

st.subheader("📈 Classification Report")
st.text(classification_report(y_test, y_pred))

st.subheader("🧩 Confusion Matrix")
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(fig)

# Prediction
st.subheader("💬 Try it yourself")
user_msg = st.text_input("Enter an SMS message:")
if user_msg:
    clean_msg = re.sub('[^a-zA-Z]', ' ', user_msg)
    clean_msg = clean_msg.lower()
    words = clean_msg.split()
    final_msg = ' '.join([ps.stem(w) for w in words if w not in stopwords.words('english')])
    vec = vectorizer.transform([final_msg]).toarray()
    pred = model.predict(vec)[0]
    result = "🚫 Spam!" if pred == 1 else "✅ Ham (Not Spam)"
    st.write("Prediction:", result)

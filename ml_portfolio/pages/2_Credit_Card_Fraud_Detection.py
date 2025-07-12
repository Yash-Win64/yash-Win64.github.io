import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from imblearn.over_sampling import SMOTE

# Streamlit title
st.title("🔒 Credit Card Fraud Detection")

st.markdown("""
This app uses the **Kaggle Credit Card Fraud Detection dataset** to predict whether a transaction is fraudulent.

It supports multiple models and handles class imbalance using **SMOTE**.
""")

# Path to dataset
file_path = "data/creditcard.csv"

try:
    df = pd.read_csv(file_path)
    st.success(f"✅ Loaded dataset from `{file_path}`")
    st.write(df.head())

    # Drop duplicates if any
    df = df.drop_duplicates()

    # Rename target column if needed
    if 'Class' not in df.columns and 'is_fraud' in df.columns:
        df.rename(columns={'is_fraud': 'Class'}, inplace=True)

    # Drop missing values and infinite values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    # Features and target
    X = df.drop('Class', axis=1)
    y = df['Class']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Apply SMOTE to handle imbalance
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    # Model selection
    model_choice = st.selectbox("🤖 Select a model", ['Logistic Regression', 'Random Forest', 'Decision Tree', 'AdaBoost'])

    if model_choice == 'Logistic Regression':
        model = LogisticRegression(max_iter=1000)
    elif model_choice == 'Random Forest':
        model = RandomForestClassifier(random_state=5)
    elif model_choice == 'Decision Tree':
        model = DecisionTreeClassifier(random_state=5)
    else:
        model = AdaBoostClassifier(random_state=5)

    # 👇 Add spinner during model training and prediction
    with st.spinner("🔄 Please wait while the model trains and makes predictions..."):
        # Train the model
        model.fit(X_resampled, y_resampled)

        # Predict
        y_pred = model.predict(X_test)

    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    st.subheader("✅ Model Accuracy")
    st.write(f"**Accuracy:** {acc:.2f}")

    # Classification Report
    st.subheader("📊 Classification Report")
    st.text(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    labels = ['Not Fraud', 'Fraud']
    st.subheader("🧩 Confusion Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    st.pyplot(fig)

    # Feature Importances (for tree-based models)
    if model_choice in ['Random Forest', 'Decision Tree', 'AdaBoost']:
        st.subheader("📌 Feature Importances")
        feature_importances = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values(by='Importance', ascending=False)
        st.bar_chart(feature_importances.set_index('Feature'))

except FileNotFoundError:
    st.error(f"❌ File not found. Please make sure `{file_path}` exists.")
except Exception as e:
    st.error(f"⚠️ Error: {e}")






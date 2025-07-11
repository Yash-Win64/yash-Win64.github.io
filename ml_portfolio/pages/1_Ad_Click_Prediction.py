import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import os

st.title("🔍 Ad Click Prediction")

st.markdown("""
Loads a predefined dataset (you can update it in `data/ad_click_dataset.csv`) to train a Random Forest model.
""")

# ✅ Load dataset directly
default_path = "data/ad_click_dataset.csv"
if os.path.exists(default_path):
    data = pd.read_csv(default_path)
    st.success("✅ Using dataset from 'data/ad_click_dataset.csv'")

    st.subheader("📄 Preview of Dataset")
    st.write(data.head())

    if 'click' in data.columns:
        # 🔹 Drop ID and full name
        data = data.drop(['id', 'full_name'], axis=1, errors='ignore')

        # 🔹 Impute missing numerical values (e.g., age)
        if 'age' in data.columns:
            data['age'] = data['age'].fillna(data['age'].median())

        # 🔹 Impute missing categorical values with mode
        for col in ['gender', 'device_type', 'ad_position', 'time_of_day']:
            if col in data.columns:
                data[col] = data[col].fillna(data[col].mode()[0])

        # 🔹 Impute browsing_history with 'Trends'
        if 'browsing_history' in data.columns:
            data['browsing_history'] = data['browsing_history'].fillna('Trends')

        # 🔹 One-hot encode all object columns except target
        categorical_cols = data.select_dtypes(include='object').columns.tolist()
        categorical_cols = [col for col in categorical_cols if col != 'click']
        data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

        # 🔹 Train/test split
        X = data.drop('click', axis=1)
        y = data['click']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # 🔹 Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # 🔹 Predict
        y_pred = model.predict(X_test)

        # 🔹 Class distribution
        st.subheader("📊 Class Distribution")
        st.bar_chart(data['click'].value_counts())

        # 🔹 Accuracy
        acc = accuracy_score(y_test, y_pred)
        st.subheader("✅ Model Accuracy")
        st.write(f"Accuracy: **{acc:.2f}**")

        # 🔹 Classification report
        report = classification_report(y_test, y_pred)
        st.subheader("📊 Classification Report")
        st.text(report)

        # 🔹 Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        labels = ['Not Clicked', 'Clicked']
        st.subheader("🧩 Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=labels, yticklabels=labels, ax=ax)
        ax.set_xlabel("Predicted Label")
        ax.set_ylabel("True Label")
        st.pyplot(fig)

        # 🔹 Feature importances
        st.subheader("📊 Feature Importances")
        importances = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values(by='Importance', ascending=False)
        st.bar_chart(importances.set_index('Feature'))

    else:
        st.error("❌ 'click' column not found in the dataset.")
else:
    st.error("❌ Dataset not found. Please place it in `data/ad_click_dataset.csv`.")


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.preprocessing import load_dataset, preprocess_data
from models.train_model import train_models

# Page config
st.set_page_config(page_title="Diabetes ML Dashboard", layout="wide")

# Sidebar
st.sidebar.title("🩺 Diabetes ML Dashboard")
st.sidebar.write("Machine Learning + Data Analysis App")

menu = st.sidebar.radio(
    "Navigation",
    ["Dataset Overview", "Data Visualization", "Model Training"]
)

# Load dataset
df = load_dataset("diabetes_prediction_dataset.csv")

# ---------------------------
# DATASET OVERVIEW
# ---------------------------
if menu == "Dataset Overview":

    st.title("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Target Variable", "Diabetes")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("Statistical Summary")
    st.write(df.describe())


# ---------------------------
# DATA VISUALIZATION
# ---------------------------
elif menu == "Data Visualization":

    st.title("📈 Data Visualization Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age Distribution")

        fig, ax = plt.subplots()
        sns.histplot(df["age"], kde=True, ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("BMI Distribution")

        fig, ax = plt.subplots()
        sns.histplot(df["bmi"], kde=True, ax=ax)
        st.pyplot(fig)

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)


# ---------------------------
# MODEL TRAINING
# ---------------------------
elif menu == "Model Training":

    st.title("🤖 Machine Learning Model Training")

    if st.button("Train Models"):

        X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

        lr, rf, lr_acc, rf_acc = train_models(X_train, X_test, y_train, y_test)

        st.success("Models Trained Successfully")

        col1, col2 = st.columns(2)

        col1.metric("Logistic Regression Accuracy", round(lr_acc, 3))
        col2.metric("Random Forest Accuracy", round(rf_acc, 3))

        # Model comparison chart
        st.subheader("Model Comparison")

        results = pd.DataFrame({
            "Model": ["Logistic Regression", "Random Forest"],
            "Accuracy": [lr_acc, rf_acc]
        })

        fig, ax = plt.subplots()
        sns.barplot(x="Model", y="Accuracy", data=results, ax=ax)
        st.pyplot(fig)
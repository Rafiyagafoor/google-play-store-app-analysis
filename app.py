import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Play Store Dashboard", layout="wide")

# Gradient Title
st.markdown(
    """
    <h1 style='text-align: center;
    background: linear-gradient(90deg,#ff4b4b,#ff9a9e,#6a11cb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;'>
    Google Play Store App Analysis and Prediction
    </h1>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Dataset Analysis", "ML Prediction"]
)

# Load dataset
df = pd.read_csv("googleplaystore.csv")

# -------- DATA CLEANING --------

df['Installs'] = df['Installs'].str.replace(',', '')
df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

df['Price'] = df['Price'].str.replace('$', '')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# ---------------- HOME ----------------

if page == "Home":

    st.subheader("Project Overview")

    st.write(
        "This dashboard analyzes Google Play Store data and predicts app installs using Machine Learning."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Apps", len(df))
    col2.metric("Average Rating", round(df['Rating'].mean(), 2))
    col3.metric("Total Categories", df['Category'].nunique())

    st.divider()

    st.subheader("Dataset Preview")
    st.dataframe(df)

# ---------------- DATASET ANALYSIS ----------------

elif page == "Dataset Analysis":

    st.subheader("Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    # Rating Distribution
    with col1:
        st.subheader("Rating Distribution")

        fig1, ax1 = plt.subplots()
        sns.histplot(df['Rating'], kde=True, bins=20, ax=ax1)

        st.pyplot(fig1)

    # Top Categories
    with col2:
        st.subheader("Top 10 App Categories")

        fig2, ax2 = plt.subplots()
        df['Category'].value_counts().head(10).plot(kind='bar', ax=ax2)

        st.pyplot(fig2)

    st.divider()

    # Installs vs Rating
    st.subheader("Installs vs Rating Trend")

    df_sorted = df.sort_values(by="Rating")

    fig3, ax3 = plt.subplots()
    sns.lineplot(x='Rating', y='Installs', data=df_sorted, ax=ax3)

    st.pyplot(fig3)

# ---------------- ML PREDICTION ----------------

elif page == "ML Prediction":

    st.subheader("Predict App Installs")

    model = joblib.load("model.pkl")

    col1, col2, col3 = st.columns(3)

    with col1:
        rating = st.slider("App Rating", 1.0, 5.0, 4.0)

    with col2:
        reviews = st.number_input("Number of Reviews", value=100)

    with col3:
        price = st.number_input("App Price", value=0)

    if st.button("Predict Installs"):

        prediction = model.predict([[rating, reviews, price]])

        st.success(f"Predicted Installs: {int(prediction[0])}")

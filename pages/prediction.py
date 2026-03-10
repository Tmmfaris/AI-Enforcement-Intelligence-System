import streamlit as st
import pickle
import pandas as pd


def show():

    st.title("🔮 Enforcement Prediction")
    st.caption("Predict expected enforcement activity using the trained ML model")

    # -----------------------------
    # Load Model
    # -----------------------------
    model = pickle.load(open("models/best_model.pkl", "rb"))
    feature_names = pickle.load(open("models/model_features.pkl", "rb"))

    # -----------------------------
    # User Inputs
    # -----------------------------
    st.subheader("Prediction Inputs")

    col1, col2 = st.columns(2)

    with col1:
        year = st.selectbox(
            "Reporting Year",
            [2021, 2022, 2023, 2024, 2025, 2026]
        )

    with col2:
        month = st.selectbox(
            "Reporting Month",
            list(range(1, 13))
        )

    # -----------------------------
    # Predict Button
    # -----------------------------
    if st.button("Generate Prediction"):

        # Create input dataframe
        input_df = pd.DataFrame(columns=feature_names)

        input_df.loc[0] = 0

        if "reporting_year" in input_df.columns:
            input_df.loc[0, "reporting_year"] = year

        if "reporting_month" in input_df.columns:
            input_df.loc[0, "reporting_month"] = month

        # -----------------------------
        # Model Prediction
        # -----------------------------
        prediction = model.predict(input_df)

        predicted_value = int(prediction[0])

        st.divider()

        # -----------------------------
        # Prediction Result
        # -----------------------------
        st.subheader("📊 Prediction Result")

        col1, col2 = st.columns(2)

        col1.metric(
            "Predicted Enforcement Value",
            f"{predicted_value:,}"
        )

        col2.metric(
            "Prediction Year",
            year
        )

        st.info(
            "This prediction estimates the expected enforcement activity based on historical trends."
        )
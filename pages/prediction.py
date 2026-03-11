import streamlit as st
import pickle
import pandas as pd
import numpy as np


def show():

    st.title("🔮 Enforcement Prediction")
    st.caption("Predict expected enforcement activity using the trained ML model")

    # Load model
    model = pickle.load(open("models/best_model.pkl", "rb"))
    feature_names = pickle.load(open("models/model_features.pkl", "rb"))

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

    if st.button("Generate Prediction"):

        input_df = pd.DataFrame(columns=feature_names)
        input_df.loc[0] = 0

        if "reporting_year" in input_df.columns:
            input_df.loc[0, "reporting_year"] = year

        if "reporting_month" in input_df.columns:
            input_df.loc[0, "reporting_month"] = month

        prediction = model.predict(input_df)

        predicted_value = int(np.expm1(prediction[0]))

        st.metric(
            "Predicted Enforcement Value",
            f"{predicted_value:,}"
        )
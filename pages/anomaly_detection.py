import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.express as px


def show():

    st.title("🚨 Enforcement Anomaly Detection")
    st.caption("Detect unusual spikes in enforcement activity using Isolation Forest")

    # -----------------------------
    # Load Data
    # -----------------------------
    df = pd.read_csv("data/clean_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    trend = df.groupby("date")["value"].sum().reset_index()

    # -----------------------------
    # Model Controls
    # -----------------------------
    st.sidebar.header("Model Settings")

    contamination = st.sidebar.slider(
        "Anomaly Sensitivity",
        min_value=0.01,
        max_value=0.10,
        value=0.05,
        step=0.01
    )

    # -----------------------------
    # Train Isolation Forest
    # -----------------------------
    model = IsolationForest(contamination=contamination, random_state=42)

    trend["anomaly"] = model.fit_predict(trend[["value"]])

    trend["anomaly_label"] = trend["anomaly"].map({1: "Normal", -1: "Anomaly"})

    # -----------------------------
    # KPI Summary
    # -----------------------------
    total_points = len(trend)
    anomaly_count = len(trend[trend["anomaly"] == -1])

    col1, col2 = st.columns(2)

    col1.metric("Total Data Points", total_points)
    col2.metric("Detected Anomalies", anomaly_count)

    st.divider()

    # -----------------------------
    # Visualization
    # -----------------------------
    st.subheader("📈 Enforcement Activity with Anomalies")

    fig = px.scatter(
        trend,
        x="date",
        y="value",
        color="anomaly_label",
        color_discrete_map={
            "Normal": "#1f77b4",
            "Anomaly": "#ff4b4b"
        },
        title="Anomaly Detection in Enforcement Activity"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -----------------------------
    # Anomaly Table
    # -----------------------------
    st.subheader("⚠️ Detected Anomalies")

    anomalies = trend[trend["anomaly"] == -1]

    if not anomalies.empty:
        st.dataframe(anomalies[["date", "value"]], use_container_width=True)
    else:
        st.info("No anomalies detected with the current model settings.")

    st.divider()

    # -----------------------------
    # Explanation
    # -----------------------------
    st.subheader("ℹ️ How This Works")

    st.write("""
Isolation Forest detects unusual patterns in data.

• Normal enforcement activity is labeled **Normal**  
• Unusual spikes or drops are labeled **Anomaly**

These anomalies may indicate:

- sudden moderation spikes
- policy enforcement changes
- platform moderation campaigns
""")
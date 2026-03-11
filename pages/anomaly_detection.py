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

    # -----------------------------
    # Create Platform Trend
    # -----------------------------
    trend = df.groupby(["date", "organization"])["value"].sum().reset_index()

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
    model = IsolationForest(
        contamination=contamination,
        random_state=42
    )

    trend["anomaly"] = model.fit_predict(trend[["value"]])

    trend["anomaly_label"] = trend["anomaly"].map({
        1: "Normal",
        -1: "Anomaly"
    })

    # -----------------------------
    # Extract anomalies
    # -----------------------------
    anomalies = trend[trend["anomaly"] == -1]

    # -----------------------------
    # KPI Summary
    # -----------------------------
    total_points = len(trend)
    anomaly_count = len(anomalies)

    col1, col2 = st.columns(2)

    col1.metric("Total Data Points", total_points)
    col2.metric("Detected Anomalies", anomaly_count)

    # -----------------------------
    # Most anomalous platform
    # -----------------------------
    if not anomalies.empty:

        top_platform = anomalies["organization"].value_counts().idxmax()

        st.metric(
            "Most Anomalous Platform",
            top_platform.capitalize()
        )

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
        symbol="organization",
        hover_data=["organization", "value"],
        title="Platform Enforcement Anomaly Detection"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -----------------------------
    # Anomaly Table
    # -----------------------------
    st.subheader("⚠️ Detected Anomalies")

    if not anomalies.empty:

        anomaly_table = anomalies[[
            "date",
            "organization",
            "value"
        ]].sort_values("date")

        anomaly_table = anomaly_table.rename(columns={
            "organization": "Platform",
            "value": "Enforcement Value"
        })

        st.dataframe(
            anomaly_table,
            use_container_width=True
        )

    else:
        st.info("No anomalies detected with the current model settings.")

    st.divider()


    # -----------------------------
    # Platform Anomaly Distribution
    # -----------------------------
    st.subheader("📊 Platform Anomaly Distribution")

    if not anomalies.empty:

        platform_counts = anomalies["organization"].value_counts().reset_index()

        platform_counts.columns = [
            "Platform",
            "Anomaly Count"
        ]

        fig_platform = px.bar(
            platform_counts,
            x="Platform",
            y="Anomaly Count",
            color="Platform",
            title="Anomalies by Platform"
        )

        st.plotly_chart(fig_platform, use_container_width=True)

    else:
        st.info("No platform anomalies detected.")



    # -----------------------------
    # Explanation
    # -----------------------------
    st.subheader("ℹ️ How This Works")

    st.write("""
Isolation Forest detects unusual patterns in enforcement activity.

• Normal enforcement behavior is labeled **Normal**  
• Unusual spikes or drops are labeled **Anomaly**

These anomalies may indicate:

- sudden moderation spikes
- policy enforcement changes
- platform moderation campaigns
""")
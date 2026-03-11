import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px


def show():

    st.title("📈 AI Enforcement Forecast")
    st.caption("Predict future enforcement activity using time-series forecasting")

    # -----------------------------
    # Load dataset
    # -----------------------------
    df = pd.read_csv("data/clean_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    # -----------------------------
    # Platform Selection
    # -----------------------------
    st.sidebar.header("Forecast Settings")

    platforms = sorted(df["organization"].unique())

    selected_platform = st.sidebar.selectbox(
        "Select Platform",
        platforms
    )

    # Filter platform
    platform_df = df[df["organization"] == selected_platform]

    trend = platform_df.groupby("date")["value"].sum().reset_index()

    # Prophet format
    trend = trend.rename(columns={
        "date": "ds",
        "value": "y"
    })

    # -----------------------------
    # Check minimum data
    # -----------------------------
    if len(trend) < 2:

        st.warning(
            f"Not enough data to forecast for **{selected_platform}**.\n\n"
            "Prophet requires at least **2 time points**."
        )

        st.dataframe(trend)
        return

    # -----------------------------
    # Forecast Horizon
    # -----------------------------
    months = st.sidebar.slider(
        "Forecast Horizon (months)",
        3,
        24,
        12
    )

    # -----------------------------
    # Train Prophet Model
    # -----------------------------
    model = Prophet()

    model.fit(trend)

    future = model.make_future_dataframe(periods=months, freq="M")

    forecast = model.predict(future)

    future_values = forecast.tail(months)

    # -----------------------------
    # Forecast KPIs
    # -----------------------------
    st.subheader(f"📊 Forecast Summary ({selected_platform})")

    avg_prediction = int(future_values["yhat"].mean())
    max_prediction = int(future_values["yhat"].max())
    min_prediction = int(future_values["yhat"].min())

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Forecast", f"{avg_prediction:,}")
    col2.metric("Highest Prediction", f"{max_prediction:,}")
    col3.metric("Lowest Prediction", f"{min_prediction:,}")

    st.divider()

    # -----------------------------
    # Forecast Chart
    # -----------------------------
    st.subheader(f"📈 Predicted Enforcement Trend ({selected_platform})")

    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title=f"{selected_platform} Enforcement Forecast"
    )

    fig.add_scatter(
        x=forecast["ds"],
        y=forecast["yhat_upper"],
        mode="lines",
        name="Upper Confidence",
        line=dict(dash="dot")
    )

    fig.add_scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        mode="lines",
        name="Lower Confidence",
        line=dict(dash="dot")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -----------------------------
    # Forecast Table
    # -----------------------------
    st.subheader("📋 Future Predictions")

    st.dataframe(
        future_values[["ds", "yhat", "yhat_lower", "yhat_upper"]],
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Explanation
    # -----------------------------
    st.subheader("ℹ️ Forecast Method")

    st.write("""
The model uses **Facebook Prophet**, a time-series forecasting algorithm.

It learns patterns from historical enforcement data and predicts future trends.

The dotted lines show **confidence intervals**, indicating possible ranges of enforcement activity.
""")
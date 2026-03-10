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

    trend = df.groupby("date")["value"].sum().reset_index()

    trend = trend.rename(columns={
        "date": "ds",
        "value": "y"
    })

    # -----------------------------
    # Forecast Settings
    # -----------------------------
    st.sidebar.header("Forecast Settings")

    months = st.sidebar.slider(
        "Forecast Horizon (months)",
        min_value=3,
        max_value=24,
        value=12
    )

    # -----------------------------
    # Train Prophet Model
    # -----------------------------
    model = Prophet()

    model.fit(trend)

    future = model.make_future_dataframe(periods=months, freq="M")

    forecast = model.predict(future)

    # -----------------------------
    # Forecast KPIs
    # -----------------------------
    st.subheader("📊 Forecast Summary")

    future_values = forecast.tail(months)

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
    st.subheader("📈 Predicted Enforcement Trend")

    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title="Forecasted Enforcement Activity"
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
The forecasting model uses **Facebook Prophet**, a time-series forecasting tool.

The model analyzes historical enforcement trends and predicts future values.

The dotted lines represent **confidence intervals**, showing the possible
range of enforcement activity.
""")
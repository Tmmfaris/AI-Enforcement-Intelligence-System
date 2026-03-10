import streamlit as st
import pandas as pd
import plotly.express as px


def show():

    st.title("📊 Enforcement Analytics Dashboard")
    st.caption("Interactive analytics for social media enforcement activity")

    # -----------------------------
    # Load dataset
    # -----------------------------
    df = pd.read_csv("data/clean_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    # -----------------------------
    # Sidebar Filters
    # -----------------------------
    st.sidebar.header("🔎 Filters")

    org_filter = st.sidebar.multiselect(
        "Organization",
        sorted(df["organization"].unique()),
        default=sorted(df["organization"].unique())
    )

    topic_filter = st.sidebar.multiselect(
        "Topic",
        sorted(df["topic"].unique()),
        default=sorted(df["topic"].unique())
    )

    year_filter = st.sidebar.multiselect(
        "Year",
        sorted(df["reporting_year"].unique()),
        default=sorted(df["reporting_year"].unique())
    )

    filtered_df = df[
        (df["organization"].isin(org_filter)) &
        (df["topic"].isin(topic_filter)) &
        (df["reporting_year"].isin(year_filter))
    ]

    # -----------------------------
    # KPI SECTION
    # -----------------------------
    st.subheader("📌 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Enforcement", f"{filtered_df['value'].sum():,.0f}")
    col2.metric("Platforms", filtered_df["organization"].nunique())
    col3.metric("Topics", filtered_df["topic"].nunique())
    col4.metric("Records", len(filtered_df))

    st.divider()

    # -----------------------------
    # TREND CHART
    # -----------------------------
    st.subheader("📈 Enforcement Trend")

    trend = filtered_df.groupby("date")["value"].sum().reset_index()

    fig_trend = px.line(
        trend,
        x="date",
        y="value",
        markers=True,
        color_discrete_sequence=["#1f77b4"]
    )

    st.plotly_chart(fig_trend, use_container_width=True)

    st.divider()

    # -----------------------------
    # PLATFORM + TOPIC ANALYSIS
    # -----------------------------
    col1, col2 = st.columns(2)

    # Platform chart
    with col1:

        st.subheader("📊 Enforcement by Platform")

        org_data = filtered_df.groupby("organization")["value"].sum().reset_index()

        fig_org = px.bar(
            org_data,
            x="organization",
            y="value",
            color="organization"
        )

        st.plotly_chart(fig_org, use_container_width=True)

    # Topic distribution
    with col2:

        st.subheader("📌 Topic Distribution")

        topic_data = filtered_df.groupby("topic")["value"].sum().reset_index()

        fig_topic = px.pie(
            topic_data,
            values="value",
            names="topic"
        )

        st.plotly_chart(fig_topic, use_container_width=True)

    st.divider()

    # -----------------------------
    # TOP TOPICS
    # -----------------------------
    st.subheader("🔥 Top Moderated Topics")

    top_topics = topic_data.sort_values(by="value", ascending=False).head(10)

    fig_top = px.bar(
        top_topics,
        x="value",
        y="topic",
        orientation="h",
        color="value",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig_top, use_container_width=True)

    st.divider()

    # -----------------------------
    # AI INSIGHTS
    # -----------------------------
    st.subheader("🧠 Automated Insights")

    if not filtered_df.empty:

        top_platform = filtered_df.groupby("organization")["value"].sum().idxmax()
        top_topic = filtered_df.groupby("topic")["value"].sum().idxmax()
        top_year = filtered_df.groupby("reporting_year")["value"].sum().idxmax()

        st.info(f"**{top_platform}** shows the highest enforcement activity.")
        st.info(f"**{top_topic}** is the most frequently moderated topic.")
        st.info(f"Enforcement actions peaked in **{top_year}**.")

    st.divider()

    # -----------------------------
    # DOWNLOAD DATA
    # -----------------------------
    st.subheader("📥 Download Filtered Data")

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="filtered_enforcement_data.csv",
        mime="text/csv",
    )
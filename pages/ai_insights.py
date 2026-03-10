import streamlit as st
import pandas as pd
import plotly.express as px


def show():

    st.title("🧠 AI Insight Generator")
    st.caption("Automatically generated insights from enforcement data")

    df = pd.read_csv("data/clean_data.csv")

    # -----------------------------
    # KPI Insights
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    total_enforcement = int(df["value"].sum())
    platforms = df["organization"].nunique()
    topics = df["topic"].nunique()
    years = df["reporting_year"].nunique()

    col1.metric("Total Enforcement", f"{total_enforcement:,}")
    col2.metric("Platforms", platforms)
    col3.metric("Topics", topics)
    col4.metric("Years Covered", years)

    st.divider()

    # -----------------------------
    # Platform Insight
    # -----------------------------
    st.subheader("📊 Platform Insights")

    platform_data = df.groupby("organization")["value"].sum().reset_index()

    top_platform = platform_data.sort_values(
        by="value", ascending=False
    ).iloc[0]["organization"]

    fig_platform = px.bar(
        platform_data,
        x="organization",
        y="value",
        color="organization",
        title="Enforcement by Platform"
    )

    st.plotly_chart(fig_platform, use_container_width=True)

    st.info(f"**{top_platform}** shows the highest enforcement activity among platforms.")

    st.divider()

    # -----------------------------
    # Topic Insights
    # -----------------------------
    st.subheader("📌 Topic Insights")

    topic_data = df.groupby("topic")["value"].sum().reset_index()

    top_topic = topic_data.sort_values(
        by="value", ascending=False
    ).iloc[0]["topic"]

    fig_topic = px.pie(
        topic_data,
        values="value",
        names="topic",
        title="Topic Distribution"
    )

    st.plotly_chart(fig_topic, use_container_width=True)

    st.info(f"**{top_topic}** is the most frequently moderated content category.")

    st.divider()

    # -----------------------------
    # Yearly Insights
    # -----------------------------
    st.subheader("📈 Yearly Enforcement Trends")

    year_data = df.groupby("reporting_year")["value"].sum().reset_index()

    top_year = year_data.sort_values(
        by="value", ascending=False
    ).iloc[0]["reporting_year"]

    fig_year = px.line(
        year_data,
        x="reporting_year",
        y="value",
        markers=True,
        title="Enforcement by Year"
    )

    st.plotly_chart(fig_year, use_container_width=True)

    st.info(f"The highest enforcement activity occurred in **{top_year}**.")

    st.divider()

    # -----------------------------
    # Top Topics Table
    # -----------------------------
    st.subheader("🔥 Top 5 Moderated Topics")

    top_topics = topic_data.sort_values(
        by="value", ascending=False
    ).head(5)

    st.dataframe(top_topics, use_container_width=True)

    st.divider()

    # -----------------------------
    # AI Summary
    # -----------------------------
    st.subheader("📑 AI Summary")

    st.success(f"""
Key Insights from Enforcement Data:

• **{top_platform}** has the highest moderation activity across platforms.  
• **{top_topic}** is the most frequently moderated harmful content category.  
• Enforcement actions peaked in **{top_year}**.  
• The dataset contains **{total_enforcement:,}** total enforcement actions.

These insights highlight how moderation policies and enforcement intensity vary
across platforms and content categories.
""")
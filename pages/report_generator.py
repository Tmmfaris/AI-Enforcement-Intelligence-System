import streamlit as st
import pandas as pd
import plotly.express as px


def show():

    st.title("📑 AI Report Generator")
    st.caption("Automatically generate an analytics report from enforcement data")

    df = pd.read_csv("data/clean_data.csv")

    if st.button("Generate Enforcement Report"):

        # -----------------------------
        # Key Metrics
        # -----------------------------
        total = df["value"].sum()
        platforms = df["organization"].nunique()
        topics = df["topic"].nunique()

        top_platform = df.groupby("organization")["value"].sum().idxmax()
        top_topic = df.groupby("topic")["value"].sum().idxmax()
        top_year = df.groupby("reporting_year")["value"].sum().idxmax()

        st.success("Report Generated")

        st.divider()

        # -----------------------------
        # KPI Section
        # -----------------------------
        st.subheader("📊 Key Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Enforcement", f"{total:,.0f}")
        col2.metric("Platforms", platforms)
        col3.metric("Topics", topics)

        st.divider()

        # -----------------------------
        # Platform Analysis
        # -----------------------------
        st.subheader("📊 Enforcement by Platform")

        platform_data = df.groupby("organization")["value"].sum().reset_index()

        fig_platform = px.bar(
            platform_data,
            x="organization",
            y="value",
            color="organization"
        )

        st.plotly_chart(fig_platform, use_container_width=True)

        st.divider()

        # -----------------------------
        # Topic Analysis
        # -----------------------------
        st.subheader("📌 Topic Distribution")

        topic_data = df.groupby("topic")["value"].sum().reset_index()

        fig_topic = px.pie(
            topic_data,
            values="value",
            names="topic"
        )

        st.plotly_chart(fig_topic, use_container_width=True)

        st.divider()

        # -----------------------------
        # Written Report
        # -----------------------------
        st.subheader("📄 Generated Report")

        report_text = f"""
### Enforcement Analytics Report

Total enforcement actions recorded: **{total:,.0f}**

Key Findings:

• **{top_platform}** has the highest enforcement activity  
• **{top_topic}** is the most moderated topic  
• Enforcement activity peaked in **{top_year}**

Insights:

Content moderation activity varies significantly across platforms and content categories.  
These insights help evaluate moderation strategies and identify areas requiring stronger enforcement.
"""

        st.markdown(report_text)

        st.divider()

        # -----------------------------
        # Download Report
        # -----------------------------
        st.subheader("📥 Download Report")

        st.download_button(
            label="Download Report (TXT)",
            data=report_text,
            file_name="enforcement_report.txt"
        )
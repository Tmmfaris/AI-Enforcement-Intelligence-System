import streamlit as st
import pandas as pd
import plotly.express as px


def show():

    st.header("🤖 AI Data Analyst")

    df = pd.read_csv("data/clean_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    question = st.text_input("Ask anything about enforcement data")

    if question:

        q = question.lower()

        # ---------------------------
        # Dataset structure
        # ---------------------------
        if "column" in q:

            st.success("Dataset Columns:")
            st.write(list(df.columns))


        # ---------------------------
        # Show dataset
        # ---------------------------
        elif "show data" in q or "dataset" in q:

            st.dataframe(df.head(50))


        # ---------------------------
        # Platform analysis
        # ---------------------------
        elif "platform" in q or "organization" in q:

            data = df.groupby("organization")["value"].sum().reset_index()

            fig = px.bar(
                data,
                x="organization",
                y="value",
                color="organization",
                title="Enforcement by Platform"
            )

            st.plotly_chart(fig, use_container_width=True)


        # ---------------------------
        # Topic analysis
        # ---------------------------
        elif "topic" in q:

            data = df.groupby("topic")["value"].sum().reset_index()

            fig = px.pie(
                data,
                values="value",
                names="topic",
                title="Topic Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)


        # ---------------------------
        # Trend analysis
        # ---------------------------
        elif "trend" in q or "time" in q or "over time" in q:

            data = df.groupby("date")["value"].sum().reset_index()

            fig = px.line(
                data,
                x="date",
                y="value",
                title="Enforcement Trend"
            )

            st.plotly_chart(fig, use_container_width=True)


        # ---------------------------
        # Year comparison
        # ---------------------------
        elif "year" in q:

            data = df.groupby("reporting_year")["value"].sum().reset_index()

            fig = px.bar(
                data,
                x="reporting_year",
                y="value",
                title="Enforcement by Year"
            )

            st.plotly_chart(fig, use_container_width=True)


        # ---------------------------
        # Top topics
        # ---------------------------
        elif "top topic" in q or "most violation" in q:

            top = df.groupby("topic")["value"].sum().sort_values(ascending=False).head(10)

            st.write("Top Moderated Topics")
            st.dataframe(top)


        # ---------------------------
        # Best platform
        # ---------------------------
        elif "best platform" in q or "highest enforcement" in q:

            result = df.groupby("organization")["value"].sum().sort_values(ascending=False)

            st.write("Platform Ranking")
            st.dataframe(result)

            st.success(f"Top Platform: **{result.index[0]}**")


        # ---------------------------
        # AI Insights
        # ---------------------------
        elif "insight" in q or "summary" in q:

            top_platform = df.groupby("organization")["value"].sum().idxmax()
            top_topic = df.groupby("topic")["value"].sum().idxmax()
            top_year = df.groupby("reporting_year")["value"].sum().idxmax()

            st.success(f"""
### Key Insights

• **{top_platform}** has the highest enforcement activity  
• **{top_topic}** is the most moderated topic  
• Enforcement peaked in **{top_year}**
""")


        # ---------------------------
        # Compare platforms
        # ---------------------------
        elif "compare" in q:

            data = df.groupby(["organization", "reporting_year"])["value"].sum().reset_index()

            fig = px.line(
                data,
                x="reporting_year",
                y="value",
                color="organization",
                title="Platform Comparison Over Time"
            )

            st.plotly_chart(fig, use_container_width=True)


        else:

            st.info("""
Try questions like:

• Show enforcement by platform  
• Plot topic distribution  
• Show enforcement trend  
• Compare platforms  
• Show enforcement by year  
• Generate insights  
• Show dataset columns  
""")
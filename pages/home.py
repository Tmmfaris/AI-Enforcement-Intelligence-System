import streamlit as st


def show():

    st.title("🚀 AI Enforcement Intelligence System")

    st.markdown("""
### AI-Powered Social Media Moderation Analytics Platform

Analyze **social media enforcement trends** using machine learning,
anomaly detection, and forecasting techniques.
""")

    st.divider()

    st.header("✨ Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
📊 **Analytics Dashboard**

Explore enforcement trends,
platform comparisons, and topic distribution.
""")

    with col2:
        st.info("""
🔮 **Machine Learning Prediction**

Predict future enforcement activity
using trained ML models.
""")

    with col3:
        st.info("""
🚨 **Anomaly Detection**

Identify unusual spikes in
moderation activity.
""")

    col4, col5 = st.columns(2)

    with col4:
        st.info("""
📈 **Forecasting**

Predict future moderation trends
using time-series forecasting.
""")

    with col5:
        st.info("""
🧠 **AI Insight Generator**

Automatically generate insights
from enforcement data.
""")

    st.divider()

    st.header("🧩 System Modules")

    st.markdown("""
1️⃣ **Analytics Dashboard** – Explore moderation activity  
2️⃣ **Prediction System** – Predict enforcement values  
3️⃣ **Anomaly Detection** – Detect unusual spikes  
4️⃣ **Forecasting Module** – Forecast future activity  
5️⃣ **AI Insight Generator** – Extract insights  
6️⃣ **Report Generator** – Generate enforcement reports
""")

    st.divider()

    st.header("⚙️ Technologies Used")

    st.markdown("""
- Python  
- Streamlit  
- Scikit-learn  
- Prophet  
- Plotly  
- Pandas
""")

    st.divider()

    st.success(
        "Use the **Navigation menu on the left** to explore the analytics system."
    )
import streamlit as st

# Import pages
from pages import home
from pages import dashboard
from pages import prediction
from pages import anomaly_detection
from pages import ai_assistant
from pages import ai_insights
from pages import forecast
from pages import report_generator


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Enforcement Intelligence System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# Custom Styling
# -------------------------------------------------

st.markdown("""
<style>

/* Hide default Streamlit page navigation */
[data-testid="stSidebarNav"] {display:none;}

/* App background */
.stApp {
    background-color: #0f172a;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#020617,#0f172a);
    border-right: 1px solid #1e293b;
}

/* Sidebar text */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] p {
    color: #cbd5f5;
}

/* Navigation menu spacing */
.stRadio > div {
    gap: 6px;
}

/* Navigation menu buttons */
.stRadio label {
    background: #111827;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #1e293b;
}

/* Hover effect */
.stRadio label:hover {
    background: #1e293b;
    border-color: #6366f1;
}

/* Selected menu item */
.stRadio input:checked + div {
    background: linear-gradient(90deg,#6366f1,#22c55e);
    color: white;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg,#111827,#020617);
    border: 1px solid #1e293b;
    padding: 20px;
    border-radius: 12px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg,#6366f1,#22c55e);
    color: white;
    border-radius: 8px;
    border: none;
}

/* Titles */
h1, h2, h3 {
    color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.image(
    "https://img.icons8.com/color/96/combo-chart.png",
    width=60
)

st.sidebar.title("AI Enforcement")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "",
    [
        "Home",
        "Analytics Dashboard",
        "Prediction",
        "Anomaly Detection",
        "Forecast",
        "AI Data Analyst",
        "AI Insights",
        "Report Generator"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

st.sidebar.caption("AI Enforcement Intelligence System")


# -------------------------------------------------
# Page Routing
# -------------------------------------------------

if page == "Home":
    home.show()

elif page == "Analytics Dashboard":
    dashboard.show()

elif page == "Prediction":
    prediction.show()

elif page == "Anomaly Detection":
    anomaly_detection.show()

elif page == "Forecast":
    forecast.show()

elif page == "AI Data Analyst":
    ai_assistant.show()

elif page == "AI Insights":
    ai_insights.show()

elif page == "Report Generator":
    report_generator.show()
# AI Enforcement Intelligence System

AI-powered analytics platform for analyzing **social media enforcement and moderation data** using **Machine Learning, Forecasting, and AI-driven insights**.

This project provides an **interactive dashboard** that helps explore moderation patterns, detect anomalies, predict enforcement activity, and generate automated reports.

---

# Features

### Analytics Dashboard

Interactive visualizations for:

* Enforcement trends over time
* Platform comparison
* Topic distribution
* Top moderated topics

### Prediction System

Machine learning model predicts enforcement activity based on historical data.

### Anomaly Detection

Detects unusual spikes or drops in enforcement activity using **Isolation Forest**.

### Forecasting

Predicts future enforcement trends using **Facebook Prophet time-series forecasting**.

### AI Data Analyst

Natural language interface allowing users to ask questions about the dataset.

Example queries:

* Which platform has the highest enforcement?
* Show enforcement trend
* What topics have the most violations?

### AI Insight Generator

Automatically extracts key insights from the dataset.

### AI Report Generator

Generates structured analytics reports summarizing enforcement patterns.

---

# Project Architecture

```
AI_Enforcement_Intelligence_System
│
├── app.py
│
├── data
│   └── clean_data.csv
│
├── models
│   ├── best_model.pkl
│   └── model_features.pkl
│
└── pages
    ├── home.py
    ├── dashboard.py
    ├── prediction.py
    ├── anomaly_detection.py
    ├── forecast.py
    ├── ai_assistant.py
    ├── ai_insights.py
    └── report_generator.py
```

---

# Installation

### Navigate to the project

```
cd AI-Enforcement-Intelligence-System
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

# Machine Learning Models

* **Random Forest Regressor** – enforcement prediction
* **Isolation Forest** – anomaly detection
* **Prophet** – time series forecasting

---

# Example Insights

* Instagram shows the highest enforcement activity
* Adult Nudity and Sexual Activity is the most moderated topic
* Enforcement activity peaked in recent years

---

# Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* Scikit-learn
* Prophet

---

# Future Improvements

* Deploy real LLM-based AI analyst
* Real-time moderation data pipeline
* Advanced forecasting models
* Interactive AI report generation

---

# Author

**Muhammed Faris T M**

Physics Postgraduate
Data Science & Analytics Enthusiast

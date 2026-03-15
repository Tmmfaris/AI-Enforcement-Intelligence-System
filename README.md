# AI Enforcement Intelligence System

An **AI-powered social media moderation analytics platform** designed to analyze enforcement trends, detect anomalies, predict moderation activity, and generate automated insights from moderation datasets.

The system provides an **interactive analytics dashboard** powered by Machine Learning, Anomaly Detection, and Time-Series Forecasting.

This project demonstrates skills in:

- Data Analytics
- Machine Learning
- Anomaly Detection
- Time Series Forecasting
- AI-powered Data Insights
- Streamlit Dashboard Development
- Cloud Deployment

---

# Live Demo

🔗 **Live Application**

https://ai-enforcement-intelligence-system-7vhnlmmt9hc8oc3hswqz36.streamlit.app/

---

# Google Colab Notebook

The full **data analysis and machine learning workflow** used in this project is available in Google Colab.

🔗 **Open in Colab**

https://colab.research.google.com/drive/1eG1ZHdDVq_jHB-uR3hUFiQoqho-TrhZU?usp=sharing

The notebook includes:

- Dataset preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Machine learning model training
- Anomaly detection experimentation
- Forecasting model preparation

---

# Problem Statement

Social media platforms generate large volumes of moderation and enforcement data.  
Analyzing these datasets manually is difficult and time-consuming.

This project builds an **AI-powered analytics system** that helps:

- Understand moderation trends
- Detect abnormal moderation patterns
- Predict future enforcement activity
- Automatically generate insights from the dataset

---

# Key Features

## Analytics Dashboard

Interactive visualizations for:

- Enforcement trends over time
- Platform comparison
- Topic distribution
- Top moderated topics

Built using **Plotly interactive charts**.

---

## Machine Learning Prediction

A regression-based ML model predicts future enforcement activity using historical moderation data.

Model Used:

- **Random Forest Regressor**

---

## Anomaly Detection

Detects unusual spikes or drops in moderation activity using:

- **Isolation Forest**

This helps identify abnormal enforcement behavior.

---

## Forecasting System

Predicts future moderation trends using **time-series forecasting**.

Model Used:

- **Facebook Prophet**

Forecast visualizations allow users to analyze future moderation patterns.

---

## AI Data Analyst

A natural language interface that allows users to query the dataset.

Example queries:

- Which platform has the highest enforcement?
- Show enforcement trend
- What topics have the most violations?

---

## AI Insight Generator

Automatically extracts key insights from the moderation dataset such as:

- Most moderated platform
- Most common violation topics
- Enforcement activity patterns

---

## AI Report Generator

Generates structured reports summarizing moderation analytics including:

- Platform comparison
- Topic distribution
- Trend analysis
- Future predictions

---

# Tech Stack

## Programming Language
- Python

## Framework
- Streamlit

## Data Processing
- Pandas
- NumPy

## Machine Learning
- Scikit-learn

## Visualization
- Plotly

## Forecasting
- Facebook Prophet

## Deployment
- Streamlit Cloud

---

# Project Structure

```
AI-Enforcement-Intelligence-System
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

# Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Tmmfaris/AI-Enforcement-Intelligence-System.git
```

```
cd AI-Enforcement-Intelligence-System
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Run the Application

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# Machine Learning Models

| Model | Purpose |
|-----|-----|
| Random Forest Regressor | Enforcement prediction |
| Isolation Forest | Anomaly detection |
| Prophet | Time-series forecasting |

---

# Example Insights

Example analytics extracted from the dataset:

- Instagram shows the highest enforcement activity
- Adult Nudity and Sexual Activity is the most moderated topic
- Enforcement activity increased significantly in recent years

---

# Future Improvements

- LLM-powered AI Data Analyst
- Real-time moderation data pipeline
- Advanced forecasting models
- Automated PDF report generation
- Real-time dashboard monitoring

---

# Author

**Muhammed Faris T M**

Physics Postgraduate  
Data Science & Analytics Enthusiast  

🔗 LinkedIn  
http://www.linkedin.com/in/muhammed-faris-tm-ab1233196

🔗 GitHub  
https://github.com/Tmmfaris

---

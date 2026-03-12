# 💸 Financial Freedom System

An AI-powered system designed to detect unfair loan structures and protect borrowers from EMI traps.

This project was inspired by a real-world problem where borrowers are often locked into loan structures that make early closure extremely expensive.

The system analyzes loan parameters and predicts financial risk using a hybrid rule + machine learning approach.

---

# Key Features

• Detects potential **EMI traps and unfair loan structures**

• Predicts **loan foreclosure risk**

• Explains **why a loan may be dangerous** using explainable AI

• Provides **financial insights through a dashboard**

• Logs patterns that indicate potential financial abuse

---

# System Architecture

Backend: FastAPI REST API  
Frontend: Streamlit dashboard  
ML: Scikit-learn models  
Explainability: Feature contribution analysis

---

# Architecture:

Frontend (Streamlit)
↓
FastAPI Backend
↓
Loan Risk Engine
↓
ML + Rule Based Analysis

---

Python  
FastAPI  
Streamlit  
Scikit-Learn  
Pandas  
NumPy

---

# API Example

POST /analyze-loan

Input:

{
  "loan_amount": 500000,
  "interest_rate": 12,
  "tenure_years": 10
}

Output:

{
  "risk_score": 0.82,
  "emi_trap": true,
  "explanation": "High interest + long tenure increases repayment burden"
}

---

# Run Locally

Clone repository

git clone <repo_url>

Install dependencies

pip install -r requirements.txt

Run backend

python -m src.main

Run frontend

streamlit run frontend/app.py

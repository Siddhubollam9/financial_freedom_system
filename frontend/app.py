import streamlit as st
import requests

st.set_page_config(page_title="Financial Freedom System", layout="centered")

st.title("💸 Financial Freedom System")

tabs = st.tabs(["EMI Trap Checker", "Loan Freedom Predictor"])

API_URL = "http://127.0.0.1:8000"

# ---------------- EMI TAB ----------------
with tabs[0]:
    st.header("EMI Trap Checker")

    product_price = st.number_input("Product Price (₹)", min_value=1)
    monthly_emi = st.number_input("Monthly EMI (₹)", min_value=1)
    tenure = st.number_input("Tenure (Months)", min_value=1)
    fee = st.number_input("Processing Fee (₹)", min_value=0)

    if st.button("Check EMI Risk"):
        payload = {
            "product_price": product_price,
            "monthly_emi": monthly_emi,
            "tenure_months": tenure,
            "processing_fee": fee
        }

        res = requests.post(f"{API_URL}/emi-risk", json=payload)
        data = res.json()

        st.success(f"Total Paid: ₹{data['total_paid']}")
        st.warning(f"Extra Paid: ₹{data['extra_paid']}")
        st.error(f"Rule-Based Risk: {data['risk_level']}")

        ml = data.get("ml_prediction")
        if ml:
            st.info(f"ML Risk: {ml['label']} (Confidence: {ml['confidence']*100}%)")

        
        


# ---------------- LOAN TAB ----------------
with tabs[1]:
    st.header("Loan Freedom Predictor")

    loan_amt = st.number_input("Loan Amount (₹)", min_value=1)
    rate = st.number_input("Interest Rate (%)", min_value=1.0)
    years = st.number_input("Total Tenure (Years)", min_value=1)
    paid = st.number_input("Years Paid", min_value=0)
    foreclose = st.number_input("Foreclosure Fee (%)", min_value=0)
    if st.button("Check Loan Status"):
        payload = {
            "loan_amount": loan_amt,
            "interest_rate": rate,
            "tenure_years": years,
            "years_paid": paid,
            "foreclosure_fee_percent": foreclose
        }

        res = requests.post(f"{API_URL}/loan-risk", json=payload)
        data = res.json()

        st.success(f"Principal Remaining: ₹{data['principal_remaining']}")
        st.error(f"Foreclosure Amount: ₹{data['foreclosure_amount']}")
        ml = data.get("ml_prediction")
        if ml:
            st.info(f"ML Loan Risk: {ml['label']} (Confidence: {ml['confidence']*100}%)")
        st.subheader("Why this risk?")
        for r in data["explanation"]:
            st.warning(r)

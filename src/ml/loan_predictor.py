import joblib
import pandas as pd
import numpy as np

model = joblib.load("src/ml/loan_risk_model.pkl")

def predict_loan_risk(loan_amt, rate, tenure, years_paid, remaining, foreclosure):
    data = pd.DataFrame([{
        "loan_amount": loan_amt,
        "interest": rate,
        "tenure": tenure,
        "years_paid": years_paid,
        "remaining": remaining,
        "foreclosure": foreclosure
    }])

    probs = model.predict_proba(data)[0]
    pred = np.argmax(probs)

    return {
        "label": ["LOW","MEDIUM","HIGH"][pred],
        "confidence": round(float(probs[pred]),2)
    }

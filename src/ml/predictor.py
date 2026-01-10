import joblib
import pandas as pd
import numpy as np

model = joblib.load("src/ml/emi_risk_model.pkl")
print("ML model loaded successfully")

def predict_emi_risk(product_price, monthly_emi, tenure, fee, extra_paid):
    data = pd.DataFrame([{
        "product_price": product_price,
        "monthly_emi": monthly_emi,
        "tenure": tenure,
        "fee": fee,
        "extra_paid": extra_paid
    }])

    probs = model.predict_proba(data)[0]
    pred = np.argmax(probs)

    return {
        "label": ["LOW", "MEDIUM", "HIGH"][pred],
        "confidence": round(float(probs[pred]), 2)
    }

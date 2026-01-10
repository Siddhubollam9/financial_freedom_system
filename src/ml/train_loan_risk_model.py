import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/loan_cases.csv")

df["risk_code"] = df["risk_label"].map({"LOW":0,"MEDIUM":1,"HIGH":2})

X = df[["loan_amount","interest","tenure","years_paid","remaining","foreclosure"]]
y = df["risk_code"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

joblib.dump(model,"src/ml/loan_risk_model.pkl")
print("Loan ML model trained")

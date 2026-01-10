import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/emi_cases.csv")

df["risk_code"] = df["risk"].map({"LOW":0, "MEDIUM":1, "HIGH":2})

X = df[["product_price","monthly_emi","tenure","fee","extra_paid"]]
y = df["risk_code"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "src/ml/emi_risk_model.pkl")

import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def log_emi_case(req, result):
    file = DATA_DIR / "emi_cases.csv"
    is_new = not file.exists()

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["timestamp","product_price","monthly_emi","tenure","fee","total_paid","extra_paid","risk"])
        writer.writerow([
            datetime.now(), req.product_price, req.monthly_emi,
            req.tenure_months, req.processing_fee,
            result["total_paid"], result["extra_paid"], result["risk_level"]
        ])

def log_loan_case(req, result):
    file = DATA_DIR / "loan_cases.csv"
    is_new = not file.exists()

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["timestamp","loan_amount","interest","tenure","years_paid","remaining","foreclosure"])
        writer.writerow([
            datetime.now(), req.loan_amount, req.interest_rate,
            req.tenure_years, req.years_paid,
            result["principal_remaining"], result["foreclosure_amount"]
        ])

from fastapi import FastAPI
from src.core.schemas import EMIRequest, LoanRequest
from src.services.risk_engine import emi_risk_service, loan_risk_service

app = FastAPI(title="Financial Freedom System API")

@app.post("/emi-risk")
def emi_risk(req: EMIRequest):
    return emi_risk_service(req)

@app.post("/loan-risk")
def loan_risk(req: LoanRequest):
    return loan_risk_service(req)

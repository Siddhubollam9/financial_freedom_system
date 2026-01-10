from src.core.emi import calculate_total_payment, calculate_emi_risk
from src.core.loan import calculate_remaining_principal
from src.utils.logger import get_logger
from src.utils.data_logger import log_emi_case, log_loan_case
from src.ml.predictor import predict_emi_risk
from src.ml.loan_predictor import predict_loan_risk
from src.core.explain import explain_loan_risk

logger = get_logger("risk_engine")

def emi_risk_service(req):
    logger.info("Processing EMI risk request")

    total = calculate_total_payment(req.monthly_emi, req.tenure_months, req.processing_fee)
    result = calculate_emi_risk(req.product_price, total)

    ml_result = predict_emi_risk(
        req.product_price,
        req.monthly_emi,
        req.tenure_months,
        req.processing_fee,
        result["extra_paid"]
    )

    result["ml_prediction"] = ml_result
    log_emi_case(req, result)
    return result

def loan_risk_service(req):
    logger.info("Processing Loan risk request")

    remaining = calculate_remaining_principal(
        req.loan_amount,
        req.interest_rate,
        req.tenure_years,
        req.years_paid
    )

    foreclosure_amount = remaining * (1 + req.foreclosure_fee_percent / 100)

    ml = predict_loan_risk(
        req.loan_amount,
        req.interest_rate,
        req.tenure_years,
        req.years_paid,
        remaining,
        foreclosure_amount
    )

    explanation = explain_loan_risk(req, remaining, foreclosure_amount)

    result = {
        "principal_remaining": round(remaining, 2),
        "foreclosure_amount": round(foreclosure_amount, 2),
        "ml_prediction": ml,
        "explanation": explanation
    }

    log_loan_case(req, result)
    return result

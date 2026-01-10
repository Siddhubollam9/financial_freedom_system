def explain_loan_risk(req, remaining, foreclosure):
    tenure_ratio = req.years_paid / req.tenure_years
    loss_ratio = foreclosure / req.loan_amount

    reasons = []

    if tenure_ratio < 0.3:
        reasons.append("You have paid less than 30% of your loan tenure.")

    if loss_ratio > 1.4:
        reasons.append("Foreclosure amount is more than 40% higher than loan amount.")

    if req.interest_rate > 14:
        reasons.append("Your interest rate is very high.")

    if not reasons:
        reasons.append("Your loan structure is financially safe.")

    return reasons

'''
Understanding emi.py

This file contains the logic that exposes financial traps.

📄 Create file: src/core/emi.py

Paste this code first:

def calculate_total_payment(monthly_emi: float, tenure: int, fee: float) -> float:
    return round((monthly_emi * tenure) + fee, 2)

🔍 Deep Explanation
What is this?

This function answers one simple question:

“How much money will I actually pay in total?”

Let’s break the syntax
def calculate_total_payment(monthly_emi: float, tenure: int, fee: float) -> float:

Part	Meaning
def	Define a function
calculate_total_payment	Function name
monthly_emi: float	EMI must be number
tenure: int	Months must be integer
fee: float	Fee must be number
-> float	Output will be a number
Function body
(monthly_emi * tenure) + fee


This is basic EMI math.

If:

EMI = 4200

Months = 36

Fee = 2500

Then:

4200 × 36 + 2500 = 153700

Why round(..., 2)?

Money must have 2 decimal points.

🧠 What is happening here?
Step 1
extra = total_payment - product_price


This shows how much extra the user is paying.

Step 2
ratio = extra / product_price


If someone pays 50k extra on 1L product:

ratio = 50000 / 100000 = 0.5 (50%)

Step 3 – Risk classification
if ratio > 0.5:
    level = "HIGH"


More than 50% extra → dangerous.

Step 4 – Return result

This returns a JSON-style dictionary.
'''

def calculate_total_payment(monthly_emi: float, tenure: int, fee: float) -> float:
    return round((monthly_emi * tenure) + fee, 2)
def calculate_emi_risk(product_price: float, total_payment: float) -> dict:
    extra = total_payment - product_price
    ratio = extra / product_price

    if ratio > 0.5:
        level = "HIGH"
    elif ratio > 0.25:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "total_paid": round(total_payment, 2),
        "extra_paid": round(extra, 2),
        "risk_level": level
    }

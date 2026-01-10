''' Understanding loan.py — the Amortization Engine

This file calculates how much principal is actually left after years of paying EMI.

This is the logic that explains what happened to your father.

🔍 Deep Explanation
Step 1 — Convert yearly interest to monthly
monthly_rate = r / 1200


If interest = 12%, monthly = 12 / 1200 = 0.01

Step 2 — Calculate EMI formula
emi = (P * monthly_rate * (1 + monthly_rate) ** total_months) / \
      ((1 + monthly_rate) ** total_months - 1)


This is the official bank EMI formula.

Banks never show this.
This is why people get trapped.

Step 3 — Why we use a loop
for _ in range(paid_months):


Every EMI payment:

Interest is taken first

Only small amount goes to principal

So we simulate month by month.

Step 4 — Interest front-loading
interest = balance * monthly_rate
principal = emi - interest
balance -= principal


This shows:

EMI	Goes to Interest	Goes to Principal
First years	Huge	Very little
Later years	Small	More
Step 5 — Final output

Returns the actual remaining principal — not what the bank tells verbally.
'''

def calculate_remaining_principal(P: float, r: float, years: int, paid_years: int) -> float:
    monthly_rate = r / 1200
    total_months = years * 12
    paid_months = paid_years * 12

    emi = (P * monthly_rate * (1 + monthly_rate) ** total_months) / \
          ((1 + monthly_rate) ** total_months - 1)

    balance = P

    for _ in range(paid_months):
        interest = balance * monthly_rate
        principal = emi - interest
        balance -= principal

    return round(balance, 2)

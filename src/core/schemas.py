
'''
Why we even need schemas.py

Imagine your project like a bank counter.

People come and tell:

“I took EMI of 4200”

“My product cost is 1 lakh”

Some people will:

Type wrong numbers

Forget fields

Enter negative values

If your code trusts them blindly → your system will crash or give wrong money advice.

So we create a gatekeeper that checks everything before allowing data inside.

That gatekeeper is Pydantic Schema.

🧠 What is Pydantic?

Pydantic is a library that:

Reads user input

Converts it into Python objects

Validates everything

If input is wrong, it automatically says:

“Your input is invalid” — without you writing extra code.

This is professional backend engineering.

📄 Now open src/core/schemas.py

Write this line first:

from pydantic import BaseModel, Field

Meaning
Word	Meaning
pydantic	Validation library
BaseModel	Base class to create schemas
Field	Used to add rules like >0, default values
Now this:
class EMIRequest(BaseModel):

What is class?

A class is a blueprint.

Think of it like a form template:

Field
product_price
monthly_emi
tenure_months
processing_fee

Anyone who wants EMI risk must fill this form.

    product_price: float = Field(..., gt=0)


Let us break it completely.

Part	Meaning
product_price	Field name
:	Python type hint
float	Must be number like 100000.0
=	Assign rule
Field(...)	Required field
gt=0	Must be greater than 0

So this line says:

“User must send a positive product price. If not, reject.”

    monthly_emi: float = Field(..., gt=0)


Same meaning.

    tenure_months: int = Field(..., gt=0)


Tenure must be integer (like 12, 24, 36).

    processing_fee: float = Field(0, ge=0)

Value	Meaning
0	Default value if user doesn't send
ge=0	Greater than or equal to zero

So negative fees are impossible.

Now Loan Form.

class LoanRequest(BaseModel):


This is another form for loan prediction.

    loan_amount: float = Field(..., gt=0)


Must be positive.

    interest_rate: float = Field(..., gt=0)


Interest must exist.

    tenure_years: int = Field(..., gt=0)

    years_paid: int = Field(..., ge=0)


Years paid can be 0 but not negative.

    foreclosure_fee_percent: float = Field(0, ge=0)


Default foreclosure = 0%.
'''
from pydantic import BaseModel, Field

class EMIRequest(BaseModel):
    product_price: float = Field(..., gt=0)
    monthly_emi: float = Field(..., gt=0)
    tenure_months: int = Field(..., gt=0)
    processing_fee: float = Field(0, ge=0)

class LoanRequest(BaseModel):
    loan_amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., gt=0)
    tenure_years: int = Field(..., gt=0)
    years_paid: int = Field(..., ge=0)
    foreclosure_fee_percent: float = Field(0, ge=0)

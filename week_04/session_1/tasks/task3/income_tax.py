# Week 4, Session 1: Task 3

# You are given function income_tax_calculator and a docstring.
# Your task is to write the body of the function based on the
# details in the docstring. You can create additional functions
# to be called from within income_tax_calculator


def income_tax_calculator(annual_income):
    """
    This function calculates the tax amount for a given taxable annual income
    based on the UK tax rates and allowances. The tax is calculated
    progressively across tax bands, as per the following rates and allowances:

    Band               |  Taxable income   | Tax rate
    Personal allowance | Up to 12,570      | 0%
    Basic rate         | 12,571 to 50,270  | 20%
    Higher rate        | 50,271 to 125,140 | 40%
    Additional rate    | over 125,140      | 45%

    Key Details:
    Personal Allowance: The first £12,570 of taxable income is tax-free.
    Progressive Taxation: Income tax is applied progressively across bands.
    For example, an annual income of £25,000 would be taxed as follows:
    The first £12,570 at 0% (personal allowance).
    The remaining £12,430 (i.e., £25,000 - £12,570) at 20% (basic rate).

    Args:
        annual_income: float

    Returns:
        a float, representing the total calculated tax, rounded to
        one decimal point. You can use the round() function,
        e.g round(tax, 1) 0.0 if annual_income is not a positive integer.
    """


def income_tax_calculator(annual_income):
    """
    Calculates UK income tax based on progressive tax bands.
    """
    # Handle non-positive income
    if annual_income <= 0:
        return 0.0
    
    tax = 0.0
    remaining_income = annual_income
    
    # Tax bands: (upper_limit, rate)
    bands = [
        (12570, 0.0),    # Personal allowance
        (50270, 0.2),    # Basic rate
        (125140, 0.4),   # Higher rate
        (float('inf'), 0.45)  # Additional rate
    ]
    
    prev_limit = 0
    for limit, rate in bands:
        if remaining_income <= 0:
            break
        # Calculate taxable amount in current band
        taxable_in_band = min(remaining_income, limit - prev_limit)
        tax += taxable_in_band * rate
        # Update remaining income and previous limit
        remaining_income -= taxable_in_band
        prev_limit = limit
    
    return round(tax, 1)

# Check if the following lines produce the correct output
print(income_tax_calculator(12000))     # 0.0
print(income_tax_calculator(14000))     # 286.0
print(income_tax_calculator(25000))     # 2486.0
print(income_tax_calculator(100000))    # 27432.0

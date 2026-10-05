p = {"purchase_price": 210000,
     "estimated_rent": 1900,
     "property_taxes": 2400,
     "insurance": 1500,
     "vacancy": 0.07,
     "maintenance": 0.08,
     "capex": 0.06,
     "management": 0.08,
     "hoa": 0,
     "utilities": 0,
     "down_payment_rate": 0.25,
     "interest_rate": 7.5,
     "loan_term_years": 30,
     "closing_cost_rate": 0.03
     }


def real_analysis(p):
    price = p["purchase_price"]
    rent_m = p["estimated_rent"]
    taxes_y = p["property_taxes"]
    ins_y = p["insurance"]
    hoa_y = p["hoa"]
    uit_y = p["utilities"]
    vacancy_rate = p["vacancy"]
    maint_rate = p["maintenance"]
    capex_rate = p["capex"]
    manage_rate = p["management"]
    down_rate = p["down_payment_rate"]
    int_rate = p["interest_rate"]
    term_years = p["loan_term_years"]
    close_rate = p["closing_cost_rate"]
    gross_income = rent_m * 12
    collected_rent = gross_income * (1 - vacancy_rate)
    maint_rate_y = gross_income * maint_rate
    manage_rate_y = collected_rent * manage_rate
    capex_rate_y = gross_income * capex_rate
    opex = maint_rate_y + ins_y + capex_rate_y + manage_rate_y + taxes_y
    noi = collected_rent - opex
    down_payment = price * down_rate
    closing_cost = price * close_rate
    cash_invested = down_payment + closing_cost
    loan_amount = price - down_payment
    monthly_interest_rate = (int_rate / 100) / 12
    number_of_payments = term_years * 12
    growth = (1 + monthly_interest_rate) ** number_of_payments
    monthly_mortgage_payment = loan_amount * (
        monthly_interest_rate * growth) / (
        growth - 1)
    annual_debt_service = monthly_mortgage_payment * 12
    annual_cashflow = noi - annual_debt_service
    cap_rate = noi / price * 100
    coc_roi = annual_cashflow / cash_invested * 100
    dscr = noi / annual_debt_service
    return noi, annual_cashflow, cap_rate, coc_roi, dscr,


noi, annual_cashflow, cap_rate, coc_roi, dscr = real_analysis(
    p)

print()
print("==== DEAL REPORT ====")
print(f"The annual cash flow for this property is ${annual_cashflow:.2f}")
print(f"The cap rate on this property is {cap_rate:.1f}")
print(f"The cash roi on this property is {coc_roi:.1f}")
print(f"The dscr on this property is {dscr:.1f}")
print()
print("==== IS PROPERTY A YES OR NO? ====")
if coc_roi >= 12 and dscr >= 1.2 and cap_rate >= 7:
    print("yes")
else:
    print("NO")

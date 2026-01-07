def calculate_gross_salary(name, emp_id, basic_salary, special_allowances, bonus_percent):
   
    gross_monthly = basic_salary + special_allowances
    annual_bonus = gross_monthly * 12 * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus

    print("\n--- Employee Salary Details ---")
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Gross Monthly Salary: ₹{gross_monthly:.2f}")
    print(f"Annual Gross Salary: ₹{annual_gross:.2f}")

    return annual_gross  


def calculate_taxable_income(name, emp_id, gross_annual_salary, standard_deduction=50000):
   
    taxable_income = gross_annual_salary - standard_deduction

    print("\n--- Taxable Income Details ---")
    print(f"Gross Annual Salary: ₹{gross_annual_salary:.2f}")
    print(f"Standard Deduction: ₹{standard_deduction:.2f}")
    print(f"Taxable Income: ₹{taxable_income:.2f}")

    return taxable_income

def calculate_tax(taxable_income):
   
    # --- Tax Slabs ---
    slabs = [
        (0, 300000, 0.0),
        (300001, 600000, 0.05),
        (600001, 900000, 0.10),
        (900001, 1200000, 0.15),
        (1200001, 1500000, 0.20),
        (1500001, float('inf'), 0.30)
    ]

    tax = 0
    breakdown = []

    for lower, upper, rate in slabs:
        if taxable_income > lower:
            taxable_amount = min(upper, taxable_income) - lower
            tax_for_slab = taxable_amount * rate
            tax += tax_for_slab
            breakdown.append((lower+1, min(upper, taxable_income), rate*100, tax_for_slab))

    # --- Section 87A Rebate ---
    if taxable_income <= 700000:
        rebate = tax  # 100% rebate
        tax = 0
    else:
        rebate = 0

    # --- 4% Health and Education Cess ---
    cess = tax * 0.04
    total_tax_payable = tax + cess

    # --- Display detailed breakdown ---
    print("\n--- Tax Calculation Details ---")
    for lower, upper, rate_percent, tax_amount in breakdown:
        print(f"Income ₹{lower} - ₹{upper} @ {rate_percent}%: ₹{tax_amount:.2f}")
    if rebate > 0:
        print(f"Section 87A Rebate Applied: ₹{rebate:.2f}")
    print(f"Health & Education Cess (4%): ₹{cess:.2f}")
    print(f"Total Tax Payable: ₹{total_tax_payable:.2f}")

    return total_tax_payable

employee_name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
basic_monthly = float(input("Enter Basic Monthly Salary: ₹"))
special_allowances = float(input("Enter Special Allowances (Monthly): ₹"))
bonus_percentage = float(input("Enter Bonus Percentage (% of Gross Salary): "))

annual_gross_salary = calculate_gross_salary(
    employee_name, employee_id, basic_monthly, special_allowances, bonus_percentage
)

taxable_income = calculate_taxable_income(
    employee_name, employee_id, annual_gross_salary
)

tax_payable = calculate_tax(taxable_income)

net_salary = annual_gross_salary - tax_payable
print(f"\nNet Salary after Tax: ₹{net_salary:.2f}")

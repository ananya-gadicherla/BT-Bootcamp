import re

def validate_name(name):
    if not name.isalpha() and " " not in name:
        return False
    if len(name.strip()) == 0 or len(name) > 50:
        return False
    return True

def validate_emp_id(emp_id):
    return emp_id.isalnum() and 5 <= len(emp_id) <= 10

def validate_salary(value):
    return value > 0 and value <= 100_000_000

def validate_allowance(value):
    return 0 <= value <= 100_000_000

def validate_bonus(value):
    return 0 <= value <= 100

# Salary & Tax Calculation

def calculate_gross_salary(basic_salary, special_allowances, bonus_percent):
    gross_monthly = basic_salary + special_allowances
    annual_bonus = gross_monthly * 12 * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    return gross_monthly, annual_gross

def calculate_taxable_income(annual_gross, standard_deduction=50000):
    taxable_income = annual_gross - standard_deduction
    return taxable_income

def calculate_tax(taxable_income):
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
    rebate = 0
    if taxable_income <= 700000:
        rebate = tax
        tax = 0
    cess = tax * 0.04
    total_tax = tax + cess
    return total_tax, breakdown, rebate, cess

# Report Generation

def generate_employee_report(employee):
    print("\n" + "="*60)
    print("               Employee Tax Report")
    print("="*60)
    print(f"{'Field':35} | {'Details'}")
    print("-"*60)
    print(f"{'Name':35} | {employee['name']}")
    print(f"{'Employee ID':35} | {employee['emp_id']}")
    print(f"{'Gross Monthly Salary':35} | ₹{employee['gross_monthly']:.2f}")
    print(f"{'Annual Gross Salary':35} | ₹{employee['annual_gross']:.2f}")
    print(f"{'Taxable Income':35} | ₹{employee['taxable_income']:.2f}")
    print(f"{'Tax Payable (Breakdown)':35} |")
    for slab in employee['tax_breakdown']:
        lower, upper, rate_percent, tax_amt = slab
        print(f"  ₹{lower} - ₹{upper} @ {rate_percent:.0f}% : ₹{tax_amt:.2f}")
    if employee['rebate'] > 0:
        print(f"  Section 87A Rebate : -₹{employee['rebate']:.2f}")
    print(f"  Health & Education Cess (4%) : ₹{employee['cess']:.2f}")
    print(f"{'Total Tax Payable':35} | ₹{employee['total_tax']:.2f}")
    print(f"{'Annual Net Salary':35} | ₹{employee['net_salary']:.2f}")
    print("="*60 + "\n")


while True:
    name = input("Enter Employee Name: ").strip()
    if validate_name(name):
        break
    print("Invalid name! Must be alphabets only, max 50 chars, non-empty.")

# Employee ID
while True:
    emp_id = input("Enter Employee ID: ").strip()
    if validate_emp_id(emp_id):
        break
    print("Invalid EmpID! Must be alphanumeric, 5–10 characters.")

# Basic Salary
while True:
    try:
        basic_salary = float(input("Enter Basic Monthly Salary: ₹"))
        if validate_salary(basic_salary):
            break
        else:
            print("Invalid Basic Salary! Must be >0 and ≤ ₹1,00,00,000.")
    except:
        print("Please enter a valid number.")

# Special Allowances
while True:
    try:
        special_allowances = float(input("Enter Special Allowances (Monthly): ₹"))
        if validate_allowance(special_allowances):
            break
        else:
            print("Invalid Allowance! Must be ≥0 and ≤ ₹1,00,00,000.")
    except:
        print("Please enter a valid number.")

# Bonus Percentage
while True:
    try:
        bonus_percentage = float(input("Enter Bonus Percentage (% of Gross Salary): "))
        if validate_bonus(bonus_percentage):
            break
        else:
            print("Invalid Bonus! Must be between 0–100%.")
    except:
        print("Please enter a valid number.")

# Calculations
gross_monthly, annual_gross = calculate_gross_salary(basic_salary, special_allowances, bonus_percentage)
taxable_income = calculate_taxable_income(annual_gross)
total_tax, breakdown, rebate, cess = calculate_tax(taxable_income)
net_salary = annual_gross - total_tax

# Prepare employee data for report
employee_data = {
    'name': name,
    'emp_id': emp_id,
    'gross_monthly': gross_monthly,
    'annual_gross': annual_gross,
    'taxable_income': taxable_income,
    'tax_breakdown': breakdown,
    'rebate': rebate,
    'cess': cess,
    'total_tax': total_tax,
    'net_salary': net_salary
}

# Generate Report
generate_employee_report(employee_data)

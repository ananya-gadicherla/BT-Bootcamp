# ---------- INPUT VALIDATION ----------

# Name
while True:
    name = input("Enter Employee Name: ")
    if name.isalpha() and len(name) <= 50:
        break
    print("Invalid name! Alphabets only, max 50 characters.")

# EmpID
while True:
    emp_id = input("Enter Employee ID: ")
    if emp_id.isalnum() and 5 <= len(emp_id) <= 10:
        break
    print("Invalid EmpID! Alphanumeric, 5–10 characters.")

# Basic Salary
while True:
    basic = float(input("Enter Basic Monthly Salary: "))
    if basic > 0 and basic <= 10000000:
        break
    print("Invalid basic salary!")

# Special Allowance
while True:
    allowance = float(input("Enter Special Allowance (Monthly): "))
    if allowance >= 0 and allowance <= 10000000:
        break
    print("Invalid allowance!")

# Bonus Percentage
while True:
    bonus_percent = float(input("Enter Bonus Percentage: "))
    if 0 <= bonus_percent <= 100:
        break
    print("Invalid bonus percentage!")

# ---------- SALARY CALCULATIONS ----------

gross_monthly = basic + allowance
annual_gross = gross_monthly * 12
bonus = (bonus_percent / 100) * annual_gross
annual_gross += bonus

standard_deduction = 50000
taxable_income = annual_gross - standard_deduction
if taxable_income < 0:
    taxable_income = 0

# ---------- TAX CALCULATION ----------

tax = 0

if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

# ---------- REBATE ----------
if taxable_income <= 700000:
    tax = 0

# ---------- CESS ----------
cess = tax * 0.04
total_tax = tax + cess

# ---------- NET SALARY ----------
net_salary = annual_gross - total_tax

# ---------- REPORT ----------

print("\n---------------------------------------")
print("        EMPLOYEE TAX REPORT")
print("---------------------------------------")
print("Name               :", name)
print("Employee ID        :", emp_id)
print("Gross Monthly Pay  : ₹", round(gross_monthly, 2))
print("Annual Gross Pay   : ₹", round(annual_gross, 2))
print("Taxable Income     : ₹", round(taxable_income, 2))
print("Tax Payable        : ₹", round(total_tax, 2))
print("Annual Net Salary  : ₹", round(net_salary, 2))
print("---------------------------------------")

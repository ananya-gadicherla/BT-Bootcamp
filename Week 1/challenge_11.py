def calculate_gross_salary(name, emp_id, basic_salary, special_allowances, bonus_percent):
    gross_monthly = basic_salary + special_allowances
    annual_bonus = gross_monthly * 12 * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus

    print("\n--- Employee Salary Details ---")
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Gross Monthly Salary: ₹{gross_monthly:.2f}")
    print(f"Annual Gross Salary: ₹{annual_gross:.2f}")


employee_name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
basic_monthly = float(input("Enter Basic Monthly Salary: "))
special_allowances = float(input("Enter Special Allowances (Monthly): "))
bonus_percentage = float(input("Enter Bonus Percentage (% of Gross Salary): "))

calculate_gross_salary(employee_name, employee_id, basic_monthly, special_allowances, bonus_percentage)

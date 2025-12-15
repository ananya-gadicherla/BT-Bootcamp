# Coding Challenge 7: Program to accept name and salary. Check if their salary is >3L
# and display if they must pay tax

def check_tax(name, salary):
    if salary > 300000:
        return f"{name} must pay tax"
    else:
        return f"{name} does not need to pay tax"

name = "Mahesh"
salary = 450000

result = check_tax(name, salary)
print(result)

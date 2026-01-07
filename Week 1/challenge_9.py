#Coding Challenge 9: Program to check if a year given is a leap year or not

def is_leap_year(year):
    
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


year = 2026

if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# Leap year if divisible by 4 AND (not divisible by 100 OR divisible by 400)

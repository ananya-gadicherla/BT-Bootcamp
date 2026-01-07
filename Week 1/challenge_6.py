#Coding Challenge 6: Program to check if a number is even or odd

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = 1
result = is_even_or_odd(num)
print(f"{num} is {result}")

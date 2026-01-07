#Coding Challenge 4: Program to swap two numbers

def swap_numbers(a, b):
    a, b = b, a
    return a, b

x = 5
y = 10
print(f"Before swapping : x={x} and y={y}")
x, y = swap_numbers(x, y)
print(f"After swapping: x={x} and y={y}")

